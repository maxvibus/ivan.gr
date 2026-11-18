const {chromium}=require('playwright');const fs=require('fs'),path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:630}});
const dir='assets/sketches';let n=0;
for(const f of fs.readdirSync(dir).filter(f=>f.endsWith('.svg'))){
 const out='og/sk/'+f.replace(/\.svg$/,'.png');
 const svg=fs.readFileSync(path.join(dir,f),'utf8');
 await p.setContent(`<body style="margin:0;background:#FBF8F2;color:#0033A0;display:flex;justify-content:center;align-items:center;height:630px;overflow:hidden">${svg.replace('<svg ','<svg style="height:630px;width:auto;max-width:1200px" ')}</body>`);
 await p.screenshot({path:out});n++;}
console.log(n);await b.close();})();
