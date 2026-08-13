#!/usr/bin/env python3
import base64, os, shutil, sys
ASSETS = [
    ('__ELEVDATA__','elev.png','image/png'), ('__MEDDATA__','med.png','image/png'),
    ('__ASIADATA__','asia.png','image/png'), ('__AMERDATA__','amer.png','image/png'),
    ('__NWEUDATA__','nweu.png','image/png'), ('__NAMDATA__','nam.png','image/png'),
    ('__AUSDATA__','aus.png','image/png'), ('__INDDATA__','ind.png','image/png'),
    ('__AFRDATA__','afr.png','image/png'), ('__MEDHIDATA__','medhi.png','image/png'),
    ('__UKHIDATA__','ukhi.png','image/png'), ('__ETRUDATA__','etru.png','image/png'),
    ('__EGEODATA__','egeo.png','image/png'), ('__GIAPPDATA__','giapp.png','image/png'),
    ('__ETIOPDATA__','etiop.png','image/png'), ('__SAFRDATA__','safr.png','image/png'),
    ('__PIRIDATA__','piri.jpg','image/jpeg'), ('__MARINADATA__','marina.jpg','image/jpeg'),
    ('__ORTDATA__','ortelius.jpg','image/jpeg'), ('__ZENODATA__','zeno.jpg','image/jpeg'),
    ('__BUACHEDATA__','buache.jpg','image/jpeg'), ('__MERCDATA__','mercator.jpg','image/jpeg'),
    ('__FRAMDATA__','framauro.jpg','image/jpeg'), ('__KANGDATA__','kangnido.jpg','image/jpeg'),
    ('__WALDDATA__','waldseem.jpg','image/jpeg'), ('__IDRISIDATA__','idrisi.jpg','image/jpeg'),
    ('__CANTINODATA__','cantino.jpg','image/jpeg'), ('__HEREFDATA__','hereford.jpg','image/jpeg'),
    ('__RICCIDATA__','ricci.jpg','image/jpeg'), ('__JAVEDATA__','vallard.jpg','image/jpeg'),
]
def b64(f, m): return f'data:{m};base64,' + base64.b64encode(open(f,'rb').read()).decode()
html = open('atlante_template.html', encoding='utf-8').read()
if '--sito' in sys.argv:
    os.makedirs('sito/assets', exist_ok=True)
    for ph, f, _ in ASSETS:
        assert ph in html, ph
        html = html.replace(ph, 'assets/' + f); shutil.copy(f, 'sito/assets/' + f)
    open('sito/index.html', 'w', encoding='utf-8').write(html); print('sito/ pronto:', len(ASSETS), 'asset')
else:
    for ph, f, m in ASSETS:
        assert ph in html, ph
        html = html.replace(ph, b64(f, m))
    open('il-mondo-prima.html', 'w', encoding='utf-8').write(html)
    print('il-mondo-prima.html', round(os.path.getsize('il-mondo-prima.html')/1e6,1), 'MB')
