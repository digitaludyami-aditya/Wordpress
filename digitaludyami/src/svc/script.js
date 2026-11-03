(function(){
'use strict';
function init(){
var R=document.getElementById('du-svc');if(!R||R.hasAttribute('data-ready'))return;R.setAttribute('data-ready','');
function $(s){return R.querySelector(s)}
function $$(s){return Array.prototype.slice.call(R.querySelectorAll(s))}
function esc(t){var d=document.createElement('div');d.textContent=t==null?'':String(t);return d.innerHTML}
var WA=R.getAttribute('data-whatsapp');
function wa(m){return 'https://wa.me/'+WA+'?text='+encodeURIComponent(m)}

/* links */
$$('[data-href]').forEach(function(a){var k=a.getAttribute('data-href');a.href=k==='phone'?'tel:'+R.getAttribute('data-phone'):R.getAttribute('data-'+k)});
$$('[data-wa]').forEach(function(a){a.href=wa(a.getAttribute('data-wa'));a.target='_blank';a.rel='noopener'});

/* FAQ schema from the visible FAQ */
try{var ld=R.querySelector('script[type="application/ld+json"]'),j=JSON.parse(ld.textContent);
  j['@graph'][1].mainEntity=$$('.faqs details').map(function(d){return {'@type':'Question',name:d.querySelector('summary').textContent.trim(),acceptedAnswer:{'@type':'Answer',text:d.querySelector('p').textContent.trim()}}});
  ld.textContent=JSON.stringify(j)}catch(e){}

/* audit form: opens WhatsApp with the details filled in */
var f=$('[data-form]'),err=$('[data-err]');
f.addEventListener('submit',function(e){e.preventDefault();
  var v=function(n){return (f.elements[n].value||'').trim()},phone=v('phone').replace(/[^\d+]/g,'');
  if(!v('name')||phone.replace(/\D/g,'').length<10){err.classList.add('on');(v('name')?f.elements.phone:f.elements.name).focus();return}
  err.classList.remove('on');
  var lines=[f.getAttribute('data-intro'),'Name: '+v('name'),'Phone: '+phone];
  if(v('biz'))lines.push('Business: '+v('biz'));if(v('choice'))lines.push(f.getAttribute('data-choice').replace(/\?$/,'')+': '+v('choice'));if(v('msg'))lines.push('Goal: '+v('msg'));
  var url=wa(lines.join('\n')),win=window.open(url,'_blank');if(win)win.opener=null;else location.href=url});

/* real results (only shown when added) */
try{var cs=JSON.parse($('script[data-cases]').textContent||'[]');
  if(cs.length){$('[data-cases-out]').innerHTML=cs.map(function(c){return '<div class="case"><small>'+esc(c.industry)+'</small><h3>'+esc(c.title)+'</h3><strong>'+esc(c.result)+'</strong><p>'+esc(c.detail)+'</p></div>'}).join('');$('[data-cases-wrap]').hidden=false}}catch(e){}

/* phone sticky bar: after the hero, hidden over the footer */
var bar=$('.sbar'),hero=$('.hero'),tick=false;
function onScroll(){tick=false;var ft=document.getElementById('du-footer')||document.querySelector('footer'),fb=ft?ft.getBoundingClientRect().top:Infinity;
  bar.classList.toggle('on',hero.getBoundingClientRect().bottom<0&&fb>innerHeight)}
addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(onScroll)}},{passive:true});onScroll();
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
