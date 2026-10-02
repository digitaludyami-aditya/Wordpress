(function(){
  var root=document.getElementById('du-app');if(!root)return;
  var panel=root.querySelector('[data-pf-panel]');if(!panel)return;
  function $(s,c){return (c||root).querySelector(s)}
  function $$(s,c){return Array.prototype.slice.call((c||root).querySelectorAll(s))}
  var GROUPS=['type','tech','cat'],LABEL={type:'Type',tech:'Technology',cat:'Category'};
  var cards=$$('.du-pf-card'),grid=$('.du-pf-grid'),empty=$('.du-pf-empty'),countEl=$('[data-pf-count]'),activeEl=$('[data-pf-active]');
  var state={type:'',tech:'',cat:'',q:''};
  var reduced=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var names={};$$('.du-pf-chip',panel).forEach(function(b){names[b.getAttribute('data-g')+':'+b.getAttribute('data-v')]=b.getAttribute('data-label')});

  function matches(c,skip){
    for(var i=0;i<GROUPS.length;i++){var g=GROUPS[i];if(g===skip)continue;if(state[g]&&c.getAttribute('data-'+g)!==state[g])return false}
    if(state.q&&c.getAttribute('data-q').indexOf(state.q)<0)return false;
    return true;
  }
  function apply(first){
    var shown=0;
    cards.forEach(function(c){
      var ok=matches(c),was=!c.hidden;
      c.hidden=!ok;
      if(ok){shown++;if(!was&&!reduced&&!first){c.classList.remove('is-in');void c.offsetWidth;c.classList.add('is-in')}}
    });
    /* faceted counts: how many results each chip would give with the other filters applied */
    $$('.du-pf-chip',panel).forEach(function(b){
      var g=b.getAttribute('data-g'),v=b.getAttribute('data-v'),n=0;
      cards.forEach(function(c){if(matches(c,g)&&(!v||c.getAttribute('data-'+g)===v))n++});
      b.querySelector('i').textContent=n;
      var on=state[g]===v;b.setAttribute('aria-pressed',on?'true':'false');
      b.disabled=(n===0&&!on);
    });
    countEl.innerHTML='Showing <span>'+shown+'</span> of '+cards.length+' projects';
    var pills='',n=0;
    GROUPS.forEach(function(g){if(state[g]){n++;pills+='<button type="button" class="du-pf-pill" data-clear="'+g+'" aria-label="Remove filter '+LABEL[g]+': '+names[g+':'+state[g]]+'">'+LABEL[g]+': '+names[g+':'+state[g]]+'<svg aria-hidden="true"><use href="#dui-close"></use></svg></button>'}});
    if(state.q){n++;pills+='<button type="button" class="du-pf-pill" data-clear="q" aria-label="Clear search">Search: &ldquo;'+state.q.replace(/[<>&"]/g,'')+'&rdquo;<svg aria-hidden="true"><use href="#dui-close"></use></svg></button>'}
    if(n>1||(n&&state.q&&0))pills+='<button type="button" class="du-pf-clear" data-clear="all">Clear all</button>';
    activeEl.innerHTML=pills;
    var tog=$('.du-pf-toggle',panel);tog.classList.toggle('has',(state.type?1:0)+(state.tech?1:0)+(state.cat?1:0)>0);
    tog.querySelector('b').textContent=(state.type?1:0)+(state.tech?1:0)+(state.cat?1:0);
    empty.hidden=shown>0;grid.hidden=shown===0;
    writeHash();
  }
  function writeHash(){
    var p=[];GROUPS.forEach(function(g){if(state[g])p.push(g+'='+encodeURIComponent(state[g]))});if(state.q)p.push('q='+encodeURIComponent(state.q));
    try{history.replaceState(null,'',p.length?'#'+p.join('&'):location.pathname+location.search)}catch(e){}
  }
  function readHash(){
    var h=location.hash.replace(/^#/,'');if(!h||h.indexOf('=')<0)return;
    h.split('&').forEach(function(kv){var a=kv.split('='),k=a[0],v=decodeURIComponent(a[1]||'');if(k==='q')state.q=v.toLowerCase();else if(GROUPS.indexOf(k)>-1&&names[k+':'+v])state[k]=v});
    $('.du-pf-search input',panel).value=state.q;
  }
  panel.addEventListener('click',function(e){
    var b=e.target.closest('.du-pf-chip');
    if(b&&!b.disabled){var g=b.getAttribute('data-g'),v=b.getAttribute('data-v');state[g]=(state[g]===v)?'':v;apply()}
  });
  root.addEventListener('click',function(e){
    var c=e.target.closest('[data-clear]');
    if(c){var k=c.getAttribute('data-clear');if(k==='all'){state={type:'',tech:'',cat:'',q:''};$('.du-pf-search input',panel).value=''}else{state[k]='';if(k==='q')$('.du-pf-search input',panel).value=''}apply()}
    if(e.target.closest('[data-pf-reset]')){state={type:'',tech:'',cat:'',q:''};$('.du-pf-search input',panel).value='';apply()}
  });
  var t;$('.du-pf-search input',panel).addEventListener('input',function(e){var v=e.target.value.trim().toLowerCase();clearTimeout(t);t=setTimeout(function(){state.q=v;apply()},120)});
  var tog=$('.du-pf-toggle',panel);
  tog.addEventListener('click',function(){var o=!panel.classList.contains('is-open');panel.classList.toggle('is-open',o);tog.setAttribute('aria-expanded',o?'true':'false')});

  /* screenshots: local upload first, then a live screenshot service, then a coloured placeholder */
  $$('.du-pf-view img').forEach(function(img){
    function fail(){var fb=img.getAttribute('data-fallback');if(fb&&img.getAttribute('data-tried')!=='1'){img.setAttribute('data-tried','1');img.src=fb}else{img.parentNode.classList.add('is-failed')}}
    img.addEventListener('error',fail);
    if(img.complete&&!img.naturalWidth&&img.getAttribute('src'))fail();
  });
  /* mShots returns a tiny placeholder while it renders a new screenshot: retry once after a few seconds */
  $$('.du-pf-view img[data-ms]').forEach(function(img){
    img.addEventListener('load',function(){if(img.naturalWidth<300&&!img.getAttribute('data-retry')){img.setAttribute('data-retry','1');setTimeout(function(){img.src=img.src.split('&r=')[0]+'&r='+Date.now()},6000)}});
  });
  window.addEventListener('hashchange',function(){var h=location.hash.replace(/^#/,'');if(h.indexOf('=')<0)return;state={type:'',tech:'',cat:'',q:''};readHash();apply()});
  readHash();apply(true);
})();
