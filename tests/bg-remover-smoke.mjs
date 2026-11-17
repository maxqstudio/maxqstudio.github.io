import assert from 'node:assert/strict';
import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';
const browser=await chromium.launch({headless:true,...(process.env.BG_BROWSER_EXE?{executablePath:process.env.BG_BROWSER_EXE}:{})});
const base=process.env.TEST_BASE_URL||'http://127.0.0.1:8765';
await mkdir('artifacts/bg-remover',{recursive:true});
let checks=0;
try {
 for(const width of [320,375,768,1440]){
  const page=await browser.newPage({viewport:{width,height:1000}});
  const errors=[];page.on('pageerror',e=>errors.push(e.message));
  for(const file of ['index.html','privacy.html','terms.html','support.html']){
   const response=await page.goto(base+'/max-background-remover/'+file,{waitUntil:'networkidle'});
   assert.equal(response.status(),200);
   await page.evaluate(()=>document.fonts.ready);
   assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,'Overflow '+file+' '+width);
   assert.equal(await page.locator('nav[aria-label="Product pages"] a[aria-current="page"]').count(),1);
   assert.ok(await page.getByRole('link',{name:'support@maxqstudio.dev',exact:true}).count());
   const failures=await page.locator('img').evaluateAll(images=>images.filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src));
   assert.deepEqual(failures,[]);
   if(file==='index.html'){
    assert.equal(await page.locator('.shots figure').count(),4);
    assert.equal(await page.locator('.hero-art img').getAttribute('src'),'../images/max-background-remover/shot-2-cutout.png');
    await page.screenshot({path:'artifacts/bg-remover/product-'+width+'.png',fullPage:true});
   }
   checks++;
  }
  assert.deepEqual(errors,[]);
  await page.close();
 }
 console.log('PASS '+checks+' product-page viewport checks: no horizontal overflow, working nav, loaded images and support links.');
}finally{await browser.close();}

