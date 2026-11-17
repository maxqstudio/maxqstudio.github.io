import { chromium } from 'playwright';
import { mkdir, readFile, copyFile } from 'node:fs/promises';
import { resolve, join } from 'node:path';
const site=resolve('.'), app=resolve('../max-bg-remover-ui'), out=join(app,'store-listing');
const browser=await chromium.launch({headless:true,executablePath:process.env.BG_BROWSER_EXE});
const assets=join(site,'images/max-background-remover');
const data=async(path,type)=>'data:'+type+';base64,'+(await readFile(path)).toString('base64');
const font=await data(join(assets,'manrope.ttf'),'font/ttf');
const icon=await data(join(assets,'app-icon.svg'),'image/svg+xml');
const css='@font-face{font-family:Manrope;src:url('+font+')}*{box-sizing:border-box}body{margin:0;font-family:Manrope,sans-serif;color:#30201e;background:#fff6ef}h1,h2,p{margin:0}';
const render=async(name,w,h,body,extra='')=>{
 const page=await browser.newPage({viewport:{width:w,height:h},deviceScaleFactor:1});
 await page.setContent('<html><head><style>'+css+extra+'</style></head><body>'+body+'</body></html>');
 await page.evaluate(async()=>{await document.fonts.ready;await Promise.all([...document.images].map(x=>x.decode()));});
 await page.screenshot({path:join(out,name),omitBackground:false});await page.close();
};
await mkdir(join(out,'graphics'),{recursive:true});
await mkdir(join(out,'phone-screenshots'),{recursive:true});
await mkdir(join(out,'promotional-screens'),{recursive:true});
await render('graphics/icon-512.png',512,512,'<img src="'+icon+'" style="width:512px;height:512px">');
await copyFile(join(out,'graphics/icon-512.png'),join(assets,'icon.png'));
const names=['shot-1-home.png','shot-2-cutout.png','shot-3-refine.png','shot-4-images.png'];
const titles=['Start with your photo.','Keep your subject.','Choose what stays.','Come back to your edit.'];
const subs=['Choose a photo or take a new one.','Preview your transparent cutout.','Select an area and process it again.','Reopen saved projects in Images.'];
const imgs=[];
const portrait=await data(join(assets,'portrait-cutout.png'),'image/png');
for(let i=0;i<4;i++){
 imgs.push(await data(join(assets,names[i]),'image/png'));
 await copyFile(join(assets,names[i]),join(out,'phone-screenshots',names[i]));
 await render('promotional-screens/'+names[i],1080,1920,
 '<div class="top"><p class="brand">MAX BACKGROUND REMOVER</p><h1>'+titles[i]+'</h1><p>'+subs[i]+'</p></div><div class="phone"><img src="'+imgs[i]+'"></div>',
 '.top{padding:70px 70px 38px}h1{font-size:76px;line-height:1.1;letter-spacing:-3px;margin:25px 0}.top p{font-size:29px}.brand{font-size:20px!important;font-weight:800;letter-spacing:3px;color:#b51b65}.phone{width:624px;margin:0 auto;border:10px solid #30201e;border-radius:43px;overflow:hidden;background:#30201e}.phone img{display:block;width:100%}');
}
await render('graphics/feature-1024x500.png',1024,500,
 '<div class="copy"><p>MAX BACKGROUND REMOVER</p><h1>Your subject.<br>No background.</h1><span>Photo → Cutout → Transparent PNG</span></div><div class="portrait"><img src="'+portrait+'"></div>',
 'body{background:#ffb79c;overflow:hidden}.copy{position:absolute;left:70px;top:110px;width:520px}.copy p{font-weight:800;letter-spacing:2px;font-size:16px}.copy h1{font-size:60px;line-height:1.08;letter-spacing:-2px;margin:22px 0}.copy span{font-size:19px}.portrait{position:absolute;top:65px;right:65px;width:340px;height:370px;border:7px solid #fff;border-radius:26px;overflow:hidden;background:repeating-conic-gradient(#eee 0% 25%,#fff 0% 50%) 50%/32px 32px}.portrait img{width:100%;height:100%;object-fit:contain;object-position:center}');
await render('graphics/ui-mockup-board.png',1600,1200,
 '<header><img src="'+icon+'"><div><p>MAX BACKGROUND REMOVER</p><h1>From photo to cutout.</h1></div></header><div class="screens">'+imgs.map((src,i)=>'<figure><div class="phone"><img src="'+src+'"></div><figcaption>'+['Home','Transparent preview','Refine','Images'][i]+'</figcaption></figure>').join('')+'</div>',
 'header{padding:60px 65px;display:flex;align-items:center;gap:28px}header>img{width:90px}header p{font-size:18px;font-weight:800;color:#b51b65;letter-spacing:3px}h1{font-size:52px;letter-spacing:-2px;margin-top:10px}.screens{display:flex;gap:44px;padding:0 65px}figure{margin:0;width:334px}.phone{border:7px solid #30201e;border-radius:30px;overflow:hidden}.phone img{width:100%;display:block}figcaption{font-size:22px;font-weight:700;margin-top:18px;text-align:center}');
await copyFile(join(out,'graphics/feature-1024x500.png'),join(assets,'feature.png'));
await copyFile(join(out,'graphics/ui-mockup-board.png'),join(assets,'ui-mockup-board.png'));
await browser.close();
console.log('Rendered icon, feature graphic, 4 promotional screens and UI mockup board. Raw screenshots copied.');

