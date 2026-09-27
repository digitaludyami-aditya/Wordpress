(function(){
  'use strict';
  var root=document.getElementById('du-header');
  if(!root||root.getAttribute('data-duh-ready'))return;
  root.setAttribute('data-duh-ready','1');
  function $(s){return root.querySelector(s)}
  function $$(s){return Array.prototype.slice.call(root.querySelectorAll(s))}
  var sticky=root.getAttribute('data-duh-sticky')!=='false';
  var desktop=window.matchMedia('(min-width:1141px)');
  var finePointer=window.matchMedia('(hover:hover) and (pointer:fine)');

  /* logo fallback */
  $$('.duh-logo').forEach(function(img){
    function fail(){img.hidden=true;var f=img.nextElementSibling;if(f)f.hidden=false}
    img.addEventListener('error',fail);if(img.complete&&!img.naturalWidth)fail();
  });

  /* active page */
  function norm(p){return p.replace(/\/+$/,'')||'/'}
  var here=norm(location.pathname),sameHost=/(^|\.)digitaludyami\.com$/.test(location.hostname);
  if(sameHost){
    $$('.duh-nav>a,.duh-m-link[href],.duh-svc,.duh-m-svc').forEach(function(a){if(norm(new URL(a.href,location.href).pathname)===here)a.setAttribute('aria-current','page')});
    if(/^\/services(\/|$)/.test(here))$$('[data-duh-services],[data-duh-acc]').forEach(function(b){b.classList.add('is-current')});
  }

  /* ---------- scroll: shrink, hide on scroll down, progress ---------- */
  var shell=$('.duh-shell'),progress=$('.duh-progress'),bar=document.getElementById('wpadminbar');
  var lastY=window.pageYOffset,ticking=false;
  function onScroll(){
    ticking=false;
    var y=window.pageYOffset,max=document.documentElement.scrollHeight-window.innerHeight;
    root.classList.toggle('is-scrolled',y>24);
    if(progress)progress.style.transform='scaleX('+(max>0?Math.min(1,y/max):0)+')';
    if(sticky){
      if(bar){var b=bar.getBoundingClientRect();root.style.setProperty('--h-top',Math.max(0,b.bottom)+'px')}
      var busy=root.classList.contains('is-menu-open')||megaOpen;
      if(!busy&&y>260&&y-lastY>6)root.classList.add('is-hidden');
      else if(lastY-y>6||y<=260)root.classList.remove('is-hidden');
    }
    lastY=y;
  }
  window.addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(onScroll)}},{passive:true});
  window.addEventListener('resize',onScroll);

  /* ---------- mega menu ---------- */
  var btn=$('[data-duh-services]'),mega=$('.duh-mega'),megaOpen=false,tOpen,tClose;
  function setMega(open,focusFirst){
    clearTimeout(tOpen);clearTimeout(tClose);
    if(!btn||open===megaOpen)return;
    megaOpen=open;mega.classList.toggle('is-open',open);btn.setAttribute('aria-expanded',open?'true':'false');
    if(open)root.classList.remove('is-hidden');
    if(open&&focusFirst){var f=mega.querySelector('a');if(f)f.focus()}
  }
  if(btn&&mega){
    btn.addEventListener('click',function(){setMega(!megaOpen)});
    btn.addEventListener('keydown',function(e){if(e.key==='ArrowDown'){e.preventDefault();setMega(true,true)}});
    [btn,mega].forEach(function(el){
      el.addEventListener('mouseenter',function(){if(!finePointer.matches)return;clearTimeout(tClose);tOpen=setTimeout(function(){setMega(true)},90)});
      el.addEventListener('mouseleave',function(){if(!finePointer.matches)return;clearTimeout(tOpen);tClose=setTimeout(function(){setMega(false)},220)});
    });
    mega.addEventListener('focusout',function(e){if(e.relatedTarget&&!mega.contains(e.relatedTarget)&&e.relatedTarget!==btn)setMega(false)});
    document.addEventListener('click',function(e){if(megaOpen&&!mega.contains(e.target)&&!btn.contains(e.target))setMega(false)});
    /* arrow keys move between services inside the panel */
    mega.addEventListener('keydown',function(e){
      if(e.key!=='ArrowDown'&&e.key!=='ArrowUp')return;
      var links=Array.prototype.slice.call(mega.querySelectorAll('a')),i=links.indexOf(document.activeElement);
      if(i<0)return;e.preventDefault();links[(i+(e.key==='ArrowDown'?1:-1)+links.length)%links.length].focus();
    });
  }

  /* ---------- mobile drawer ---------- */
  var burger=$('.duh-burger'),drawer=$('.duh-drawer'),lastFocus=null;
  function setDrawer(open){
    if(open===root.classList.contains('is-menu-open'))return;
    root.classList.toggle('is-menu-open',open);
    burger.setAttribute('aria-expanded',open?'true':'false');
    document.documentElement.style.overflow=open?'hidden':'';
    if(open){lastFocus=document.activeElement;root.classList.remove('is-hidden');setTimeout(function(){$('.duh-close-btn').focus()},60)}
    else if(lastFocus&&lastFocus.focus){lastFocus.focus()}
  }
  burger.addEventListener('click',function(){setDrawer(true)});
  $$('[data-duh-close]').forEach(function(el){el.addEventListener('click',function(){setDrawer(false)})});
  $$('.duh-drawer a').forEach(function(a){a.addEventListener('click',function(){setDrawer(false)})});
  $$('[data-duh-acc]').forEach(function(b){
    var panel=document.getElementById(b.getAttribute('aria-controls'));
    b.addEventListener('click',function(){var o=b.getAttribute('aria-expanded')!=='true';b.setAttribute('aria-expanded',o?'true':'false');panel.classList.toggle('is-open',o)});
  });

  /* keyboard: Esc closes, Tab stays inside the drawer */
  document.addEventListener('keydown',function(e){
    if(e.key==='Escape'){
      if(root.classList.contains('is-menu-open')){setDrawer(false)}
      else if(megaOpen){setMega(false);btn.focus()}
      return;
    }
    if(e.key==='Tab'&&root.classList.contains('is-menu-open')){
      var f=Array.prototype.slice.call(drawer.querySelectorAll('a[href],button')).filter(function(el){return el.offsetParent!==null});
      if(!f.length)return;var first=f[0],last=f[f.length-1];
      if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus()}
      else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus()}
    }
  });
  function onBp(){setDrawer(false);setMega(false)}
  if(desktop.addEventListener)desktop.addEventListener('change',onBp);else if(desktop.addListener)desktop.addListener(onBp);
  onScroll();
})();
