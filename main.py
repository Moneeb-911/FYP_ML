import joblib

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def cluster_image(pic,points=[[0, 0, 0], [97.00881952, 72.17407544, 44.85307902],
             [108.71433554, 60.85790536, 49.73037811]]):
    pic2=pic.reshape(-1,3)
    pic2=np.array(pic2)
    km=KMeans(n_clusters=3,n_init=10, random_state=42,init=[[0,0,0],[97.00881952, 72.17407544, 44.85307902],[108.71433554,  60.85790536,  49.73037811]])
    km.fit(pic2)
    cluster_labels = km.labels_
    centroids=km.cluster_centers_
    points_centroid1 = pic2[cluster_labels == 1]
    points_centroid2 = pic2[cluster_labels == 2]
    return [centroids[1][0],centroids[1][1],centroids[1][2],centroids[2][0],centroids[2][1],centroids[2][2],len(points_centroid1),len(points_centroid2)]



pic=plt.imread('C:\\Users\\ALVI COMPUTER\\Desktop\images.jpg')
# pic=plt.imread('https://www.pexels.com/search/apple')


res=cluster_image(pic)
model=joblib.load('votig_clf.pkl')

res1=model.predict([res])

print(res1)


py 3.11.5

aiobotocore @ file:///C:/b/abs_3cwz1w13nn/croot/aiobotocore_1701291550158/work
aiohttp @ file:///C:/b/abs_27h_1rpxgd/croot/aiohttp_1707342354614/work
aioitertools @ file:///tmp/build/80754af9/aioitertools_1607109665762/work
aiosignal @ file:///tmp/build/80754af9/aiosignal_1637843061372/work
alabaster @ file:///home/ktietz/src/ci/alabaster_1611921544520/work
altair @ file:///C:/b/abs_27reu1igbg/croot/altair_1687526066495/work
anaconda-anon-usage @ file:///C:/b/abs_95v3x0wy8p/croot/anaconda-anon-usage_1697038984188/work
anaconda-catalogs @ file:///C:/b/abs_8btyy0o8s8/croot/anaconda-catalogs_1685727315626/work
anaconda-client @ file:///C:/b/abs_34txutm0ue/croot/anaconda-client_1708640705294/work
anaconda-cloud-auth @ file:///C:/b/abs_27x7fzodlx/croot/anaconda-cloud-auth_1712794918678/work
anaconda-navigator @ file:///C:/b/abs_d8d4a02c3t/croot/anaconda-navigator_1713464063970/work
anaconda-project @ file:///C:/ci_311/anaconda-project_1676458365912/work
anyio @ file:///C:/b/abs_847uobe7ea/croot/anyio_1706220224037/work
appdirs==1.4.4
archspec @ file:///croot/archspec_1709217642129/work
argon2-cffi @ file:///opt/conda/conda-bld/argon2-cffi_1645000214183/work
argon2-cffi-bindings @ file:///C:/ci_311/argon2-cffi-bindings_1676424443321/work
arrow @ file:///C:/ci_311/arrow_1678249767083/work
astroid @ file:///C:/ci_311/astroid_1678740610167/work
astropy @ file:///C:/b/abs_2fb3x_tapx/croot/astropy_1697468987983/work
asttokens @ file:///opt/conda/conda-bld/asttokens_1646925590279/work
async-lru @ file:///C:/b/abs_e0hjkvwwb5/croot/async-lru_1699554572212/work
atomicwrites==1.4.0
attrs @ file:///C:/b/abs_35n0jusce8/croot/attrs_1695717880170/work
Automat @ file:///tmp/build/80754af9/automat_1600298431173/work
autopep8 @ file:///opt/conda/conda-bld/autopep8_1650463822033/work
Babel @ file:///C:/ci_311/babel_1676427169844/work
backports.functools-lru-cache @ file:///tmp/build/80754af9/backports.functools_lru_cache_1618170165463/work
backports.tempfile @ file:///home/linux1/recipes/ci/backports.tempfile_1610991236607/work
backports.weakref==1.0.post1
bcrypt @ file:///C:/ci_311/bcrypt_1676435170049/work
beautifulsoup4 @ file:///C:/b/abs_0agyz1wsr4/croot/beautifulsoup4-split_1681493048687/work
binaryornot @ file:///tmp/build/80754af9/binaryornot_1617751525010/work
black @ file:///C:/b/abs_29gqa9a44y/croot/black_1701097690150/work
bleach @ file:///opt/conda/conda-bld/bleach_1641577558959/work
blinker @ file:///C:/b/abs_d9y2dm7cw2/croot/blinker_1696539752170/work
bokeh @ file:///C:/b/abs_74ungdyhwc/croot/bokeh_1706912192007/work
boltons @ file:///C:/ci_311/boltons_1677729932371/work
botocore @ file:///C:/b/abs_5a285dtc94/croot/botocore_1701286504141/work
Bottleneck @ file:///C:/b/abs_f05kqh7yvj/croot/bottleneck_1707864273291/work
Brotli @ file:///C:/ci_311/brotli-split_1676435766766/work
cachetools @ file:///tmp/build/80754af9/cachetools_1619597386817/work
certifi @ file:///C:/b/abs_35d7n66oz9/croot/certifi_1707229248467/work/certifi
cffi @ file:///C:/b/abs_924gv1kxzj/croot/cffi_1700254355075/work
chardet @ file:///C:/ci_311/chardet_1676436134885/work
charset-normalizer @ file:///tmp/build/80754af9/charset-normalizer_1630003229654/work
click @ file:///C:/b/abs_f9ihnt72pu/croot/click_1698129847492/work
cloudpickle @ file:///C:/b/abs_3796yxesic/croot/cloudpickle_1683040098851/work
clyent==1.2.2
colorama @ file:///C:/ci_311/colorama_1676422310965/work
colorcet @ file:///C:/ci_311/colorcet_1676440389947/work
comm @ file:///C:/ci_311/comm_1678376562840/work
conda @ file:///C:/b/abs_1e6dlkntna/croot/conda_1710772093015/work
conda-build @ file:///C:/b/abs_3ed9gavxgz/croot/conda-build_1708025907525/work
conda-content-trust @ file:///C:/b/abs_e3bcpyv7sw/croot/conda-content-trust_1693490654398/work
conda-libmamba-solver @ file:///croot/conda-libmamba-solver_1706733287605/work/src
conda-pack @ file:///tmp/build/80754af9/conda-pack_1611163042455/work
conda-package-handling @ file:///C:/b/abs_b9wp3lr1gn/croot/conda-package-handling_1691008700066/work
conda-repo-cli==1.0.75
conda-token @ file:///Users/paulyim/miniconda3/envs/c3i/conda-bld/conda-token_1662660369760/work
conda-verify==3.4.2
conda_index @ file:///croot/conda-index_1706633791028/work
conda_package_streaming @ file:///C:/b/abs_6c28n38aaj/croot/conda-package-streaming_1690988019210/work
constantly @ file:///C:/b/abs_cbuavw4443/croot/constantly_1703165617403/work
contourpy @ file:///C:/b/abs_853rfy8zse/croot/contourpy_1700583617587/work
cookiecutter @ file:///C:/b/abs_3d1730toam/croot/cookiecutter_1700677089156/work
cryptography @ file:///C:/b/abs_531eqmhgsd/croot/cryptography_1707523768330/work
cssselect @ file:///C:/b/abs_71gnjab7b0/croot/cssselect_1707339955530/work
cycler @ file:///tmp/build/80754af9/cycler_1637851556182/work
cytoolz @ file:///C:/b/abs_d43s8lnb60/croot/cytoolz_1701723636699/work
dask @ file:///C:/b/abs_1899k8plyj/croot/dask-core_1701396135885/work
datashader @ file:///C:/b/abs_cb5s63ty8z/croot/datashader_1699544282143/work
debugpy @ file:///C:/b/abs_c0y1fjipt2/croot/debugpy_1690906864587/work
decorator @ file:///opt/conda/conda-bld/decorator_1643638310831/work
defusedxml @ file:///tmp/build/80754af9/defusedxml_1615228127516/work
diff-match-patch @ file:///Users/ktietz/demo/mc3/conda-bld/diff-match-patch_1630511840874/work
dill @ file:///C:/b/abs_084unuus3z/croot/dill_1692271268687/work
distributed @ file:///C:/b/abs_5eren88ku4/croot/distributed_1701398076011/work
distro @ file:///C:/b/abs_a3uni_yez3/croot/distro_1701455052240/work
docstring-to-markdown @ file:///C:/ci_311/docstring-to-markdown_1677742566583/work
docutils @ file:///C:/ci_311/docutils_1676428078664/work
entrypoints @ file:///C:/ci_311/entrypoints_1676423328987/work
et-xmlfile==1.1.0
executing @ file:///opt/conda/conda-bld/executing_1646925071911/work
fastjsonschema @ file:///C:/ci_311/python-fastjsonschema_1679500568724/work
filelock @ file:///C:/b/abs_f2gie28u58/croot/filelock_1700591233643/work
flake8 @ file:///C:/ci_311/flake8_1678376624746/work
Flask @ file:///C:/b/abs_efc024w7fv/croot/flask_1702980041157/work
fonttools==4.25.0
frozenlist @ file:///C:/b/abs_d8e__s1ys3/croot/frozenlist_1698702612014/work
fsspec @ file:///C:/b/abs_97mpfsesn0/croot/fsspec_1701286534629/work
future @ file:///C:/ci_311_rebuilds/future_1678998246262/work
gensim @ file:///C:/ci_311/gensim_1677743037820/work
gitdb @ file:///tmp/build/80754af9/gitdb_1617117951232/work
GitPython @ file:///C:/b/abs_e1lwow9h41/croot/gitpython_1696937027832/work
gmpy2 @ file:///C:/ci_311/gmpy2_1677743390134/work
greenlet @ file:///C:/b/abs_a6c75ie0bc/croot/greenlet_1702060012174/work
h5py @ file:///C:/b/abs_17fav01gwy/croot/h5py_1691589733413/work
HeapDict @ file:///Users/ktietz/demo/mc3/conda-bld/heapdict_1630598515714/work
holoviews @ file:///C:/b/abs_704uucojt7/croot/holoviews_1707836477070/work
hvplot @ file:///C:/b/abs_3627uzd5h0/croot/hvplot_1706712443782/work
hyperlink @ file:///tmp/build/80754af9/hyperlink_1610130746837/work
idna @ file:///C:/ci_311/idna_1676424932545/work
imagecodecs @ file:///C:/b/abs_e2g5zbs1q0/croot/imagecodecs_1695065012000/work
imageio @ file:///C:/b/abs_aeqerw_nps/croot/imageio_1707247365204/work
imagesize @ file:///C:/ci_311/imagesize_1676431905616/work
imbalanced-learn @ file:///C:/b/abs_87es3kd5fi/croot/imbalanced-learn_1700648276799/work
importlib-metadata @ file:///C:/b/abs_c1egths604/croot/importlib_metadata-suite_1704813568388/work
incremental @ file:///croot/incremental_1708639938299/work
inflection==0.5.1
iniconfig @ file:///home/linux1/recipes/ci/iniconfig_1610983019677/work
intake @ file:///C:/ci_311_rebuilds/intake_1678999914269/work
intervaltree @ file:///Users/ktietz/demo/mc3/conda-bld/intervaltree_1630511889664/work
ipykernel @ file:///C:/b/abs_c2u94kxcy6/croot/ipykernel_1705933907920/work
ipython @ file:///C:/b/abs_b6pfgmrqnd/croot/ipython_1704833422163/work
ipython-genutils @ file:///tmp/build/80754af9/ipython_genutils_1606773439826/work
ipywidgets @ file:///croot/ipywidgets_1701289330913/work
isort @ file:///tmp/build/80754af9/isort_1628603791788/work
itemadapter @ file:///tmp/build/80754af9/itemadapter_1626442940632/work
itemloaders @ file:///C:/b/abs_5e3azgv25z/croot/itemloaders_1708639993442/work
itsdangerous @ file:///tmp/build/80754af9/itsdangerous_1621432558163/work
jaraco.classes @ file:///tmp/build/80754af9/jaraco.classes_1620983179379/work
jedi @ file:///C:/ci_311/jedi_1679427407646/work
jellyfish @ file:///C:/b/abs_50kgvtnrbj/croot/jellyfish_1695193564091/work
Jinja2 @ file:///C:/b/abs_f7x5a8op2h/croot/jinja2_1706733672594/work
jmespath @ file:///C:/b/abs_59jpuaows7/croot/jmespath_1700144635019/work
joblib @ file:///C:/b/abs_1anqjntpan/croot/joblib_1685113317150/work
json5 @ file:///tmp/build/80754af9/json5_1624432770122/work
jsonpatch @ file:///tmp/build/80754af9/jsonpatch_1615747632069/work
jsonpointer==2.1
jsonschema @ file:///C:/b/abs_d1c4sm8drk/croot/jsonschema_1699041668863/work
jsonschema-specifications @ file:///C:/b/abs_0brvm6vryw/croot/jsonschema-specifications_1699032417323/work
jupyter @ file:///C:/b/abs_4e102rc6e5/croot/jupyter_1707947170513/work
jupyter-console @ file:///C:/b/abs_82xaa6i2y4/croot/jupyter_console_1680000189372/work
jupyter-events @ file:///C:/b/abs_17ajfqnlz0/croot/jupyter_events_1699282519713/work
jupyter-lsp @ file:///C:/b/abs_ecle3em9d4/croot/jupyter-lsp-meta_1699978291372/work
jupyter_client @ file:///C:/b/abs_a6h3c8hfdq/croot/jupyter_client_1699455939372/work
jupyter_core @ file:///C:/b/abs_c769pbqg9b/croot/jupyter_core_1698937367513/work
jupyter_server @ file:///C:/b/abs_7esjvdakg9/croot/jupyter_server_1699466495151/work
jupyter_server_terminals @ file:///C:/b/abs_ec0dq4b50j/croot/jupyter_server_terminals_1686870763512/work
jupyterlab @ file:///C:/b/abs_43venm28fu/croot/jupyterlab_1706802651134/work
jupyterlab-pygments @ file:///tmp/build/80754af9/jupyterlab_pygments_1601490720602/work
jupyterlab-widgets @ file:///C:/b/abs_adrrqr26no/croot/jupyterlab_widgets_1700169018974/work
jupyterlab_server @ file:///C:/b/abs_e08i7qn9m8/croot/jupyterlab_server_1699555481806/work
keyring @ file:///C:/b/abs_dbjc7g0dh2/croot/keyring_1678999228878/work
kiwisolver @ file:///C:/ci_311/kiwisolver_1676431979301/work
lazy-object-proxy @ file:///C:/ci_311/lazy-object-proxy_1676432050939/work
lazy_loader @ file:///C:/b/abs_3bn4_r4g42/croot/lazy_loader_1695850158046/work
lckr_jupyterlab_variableinspector @ file:///C:/b/abs_b5yb2mprx2/croot/jupyterlab-variableinspector_1701096592545/work
libarchive-c @ file:///tmp/build/80754af9/python-libarchive-c_1617780486945/work
libmambapy @ file:///C:/b/abs_2euls_1a38/croot/mamba-split_1704219444888/work/libmambapy
linkify-it-py @ file:///C:/ci_311/linkify-it-py_1676474436187/work
llvmlite @ file:///C:/b/abs_da15r8vkf8/croot/llvmlite_1706910779994/work
lmdb @ file:///C:/b/abs_556ronuvb2/croot/python-lmdb_1682522366268/work
locket @ file:///C:/ci_311/locket_1676428325082/work
lxml @ file:///C:/b/abs_9e7tpg2vv9/croot/lxml_1695058219431/work
lz4 @ file:///C:/b/abs_064u6aszy3/croot/lz4_1686057967376/work
Markdown @ file:///C:/ci_311/markdown_1676437912393/work
markdown-it-py @ file:///C:/b/abs_a5bfngz6fu/croot/markdown-it-py_1684279915556/work
MarkupSafe @ file:///C:/b/abs_ecfdqh67b_/croot/markupsafe_1704206030535/work
matplotlib @ file:///C:/b/abs_e26vnvd5s1/croot/matplotlib-suite_1698692153288/work
matplotlib-inline @ file:///C:/ci_311/matplotlib-inline_1676425798036/work
mccabe @ file:///opt/conda/conda-bld/mccabe_1644221741721/work
mdit-py-plugins @ file:///C:/ci_311/mdit-py-plugins_1676481827414/work
mdurl @ file:///C:/ci_311/mdurl_1676442676678/work
menuinst @ file:///C:/b/abs_099kybla52/croot/menuinst_1706732987063/work
mistune @ file:///C:/ci_311/mistune_1676425111783/work
mkl-fft @ file:///C:/b/abs_19i1y8ykas/croot/mkl_fft_1695058226480/work
mkl-random @ file:///C:/b/abs_edwkj1_o69/croot/mkl_random_1695059866750/work
mkl-service==2.4.0
more-itertools @ file:///C:/b/abs_36p38zj5jx/croot/more-itertools_1700662194485/work
mpmath @ file:///C:/b/abs_7833jrbiox/croot/mpmath_1690848321154/work
msgpack @ file:///C:/ci_311/msgpack-python_1676427482892/work
multidict @ file:///C:/b/abs_44ido987fv/croot/multidict_1701097803486/work
multipledispatch @ file:///C:/ci_311/multipledispatch_1676442767760/work
munkres==1.1.4
mypy @ file:///C:/b/abs_3880czibje/croot/mypy-split_1708366584048/work
mypy-extensions @ file:///C:/b/abs_8f7xiidjya/croot/mypy_extensions_1695131051147/work
navigator-updater @ file:///C:/b/abs_895otdwmo9/croot/navigator-updater_1695210220239/work
nbclient @ file:///C:/b/abs_cal0q5fyju/croot/nbclient_1698934263135/work
nbconvert @ file:///C:/b/abs_17p29f_rx4/croot/nbconvert_1699022793097/work
nbformat @ file:///C:/b/abs_5a2nea1iu2/croot/nbformat_1694616866197/work
nest-asyncio @ file:///C:/b/abs_65d6lblmoi/croot/nest-asyncio_1708532721305/work
networkx @ file:///C:/b/abs_e6gi1go5op/croot/networkx_1690562046966/work
nltk @ file:///C:/b/abs_a638z6l1z0/croot/nltk_1688114186909/work
notebook @ file:///C:/b/abs_65xjlnf9q4/croot/notebook_1708029957105/work
notebook_shim @ file:///C:/b/abs_a5xysln3lb/croot/notebook-shim_1699455926920/work
numba @ file:///C:/b/abs_3e3co1qfvo/croot/numba_1707085143481/work
numexpr @ file:///C:/b/abs_5fucrty5dc/croot/numexpr_1696515448831/work
numpy @ file:///C:/b/abs_c1ywpu18ar/croot/numpy_and_numpy_base_1708638681471/work/dist/numpy-1.26.4-cp311-cp311-win_amd64.whl#sha256=5dfd3e04dc1c2826d3f404fdc7f93c097901f5da9b91f4f394f79d4e038ed81d
numpydoc @ file:///C:/ci_311/numpydoc_1676453412027/work
openpyxl==3.0.10
overrides @ file:///C:/b/abs_cfh89c8yf4/croot/overrides_1699371165349/work
packaging @ file:///C:/b/abs_28t5mcoltc/croot/packaging_1693575224052/work
pandas @ file:///C:/b/abs_fej9bi0gew/croot/pandas_1702318041921/work/dist/pandas-2.1.4-cp311-cp311-win_amd64.whl#sha256=d3609b7cc3e3c4d99ad640a4b8e710ba93ccf967ab8e5245b91033e0200f9286
pandocfilters @ file:///opt/conda/conda-bld/pandocfilters_1643405455980/work
panel @ file:///C:/b/abs_abnm_ot327/croot/panel_1706539613212/work
param @ file:///C:/b/abs_39ncjvb7lu/croot/param_1705937833389/work
paramiko @ file:///opt/conda/conda-bld/paramiko_1640109032755/work
parsel @ file:///C:/b/abs_ebc3tzm_c4/croot/parsel_1707503517596/work
parso @ file:///opt/conda/conda-bld/parso_1641458642106/work
partd @ file:///C:/b/abs_46awex0fd7/croot/partd_1698702622970/work
pathlib @ file:///Users/ktietz/demo/mc3/conda-bld/pathlib_1629713961906/work
pathspec @ file:///C:/ci_311/pathspec_1679427644142/work
patsy==0.5.3
pexpect @ file:///tmp/build/80754af9/pexpect_1605563209008/work
pickleshare @ file:///tmp/build/80754af9/pickleshare_1606932040724/work
pillow @ file:///C:/b/abs_e22m71t0cb/croot/pillow_1707233126420/work
pkce @ file:///C:/b/abs_d0z4444tb0/croot/pkce_1690384879799/work
pkginfo @ file:///C:/b/abs_d18srtr68x/croot/pkginfo_1679431192239/work
platformdirs @ file:///C:/b/abs_b6z_yqw_ii/croot/platformdirs_1692205479426/work
plotly @ file:///C:/ci_311/plotly_1676443558683/work
pluggy @ file:///C:/ci_311/pluggy_1676422178143/work
ply==3.11
prometheus-client @ file:///C:/ci_311/prometheus_client_1679591942558/work
prompt-toolkit @ file:///C:/b/abs_68uwr58ed1/croot/prompt-toolkit_1704404394082/work
Protego @ file:///tmp/build/80754af9/protego_1598657180827/work
protobuf==3.20.3
psutil @ file:///C:/ci_311_rebuilds/psutil_1679005906571/work
ptyprocess @ file:///tmp/build/80754af9/ptyprocess_1609355006118/work/dist/ptyprocess-0.7.0-py2.py3-none-any.whl
pure-eval @ file:///opt/conda/conda-bld/pure_eval_1646925070566/work
py-cpuinfo @ file:///C:/b/abs_9ej7u6shci/croot/py-cpuinfo_1698068121579/work
pyarrow @ file:///C:/b/abs_93i_y2dub4/croot/pyarrow_1707330894046/work/python
pyasn1 @ file:///Users/ktietz/demo/mc3/conda-bld/pyasn1_1629708007385/work
pyasn1-modules==0.2.8
pycodestyle @ file:///C:/ci_311/pycodestyle_1678376707834/work
pycosat @ file:///C:/b/abs_31zywn1be3/croot/pycosat_1696537126223/work
pycparser @ file:///tmp/build/80754af9/pycparser_1636541352034/work
pyct @ file:///C:/ci_311/pyct_1676438538057/work
pycurl==7.45.2
pydantic @ file:///C:/b/abs_9byjrk31gl/croot/pydantic_1695798904828/work
pydeck @ file:///C:/b/abs_ad9p880wi1/croot/pydeck_1706194121328/work
PyDispatcher==2.0.5
pydocstyle @ file:///C:/ci_311/pydocstyle_1678402028085/work
pyerfa @ file:///C:/ci_311/pyerfa_1676503994641/work
pyflakes @ file:///C:/ci_311/pyflakes_1678402101687/work
Pygments @ file:///C:/b/abs_fay9dpq4n_/croot/pygments_1684279990574/work
PyJWT @ file:///C:/ci_311/pyjwt_1676438890509/work
pylint @ file:///C:/ci_311/pylint_1678740302984/work
pylint-venv @ file:///C:/ci_311/pylint-venv_1678402170638/work
pyls-spyder==0.4.0
PyNaCl @ file:///C:/ci_311/pynacl_1676445861112/work
pyodbc @ file:///C:/b/abs_90kly0uuwz/croot/pyodbc_1705431396548/work
pyOpenSSL @ file:///C:/b/abs_baj0aupznq/croot/pyopenssl_1708380486701/work
pyparsing @ file:///C:/ci_311/pyparsing_1678502182533/work
PyQt5==5.15.10
PyQt5-sip @ file:///C:/b/abs_c0pi2mimq3/croot/pyqt-split_1698769125270/work/pyqt_sip
PyQtWebEngine==5.15.6
PySocks @ file:///C:/ci_311/pysocks_1676425991111/work
pytest @ file:///C:/b/abs_48heoo_k8y/croot/pytest_1690475385915/work
python-dateutil @ file:///tmp/build/80754af9/python-dateutil_1626374649649/work
python-dotenv @ file:///C:/ci_311/python-dotenv_1676455170580/work
python-json-logger @ file:///C:/b/abs_cblnsm6puj/croot/python-json-logger_1683824130469/work
python-lsp-black @ file:///C:/ci_311/python-lsp-black_1678721855627/work
python-lsp-jsonrpc==1.0.0
python-lsp-server @ file:///C:/b/abs_catecj7fv1/croot/python-lsp-server_1681930405912/work
python-slugify @ file:///tmp/build/80754af9/python-slugify_1620405669636/work
python-snappy @ file:///C:/ci_311/python-snappy_1676446060182/work
pytoolconfig @ file:///C:/b/abs_f2j_xsvrpn/croot/pytoolconfig_1701728751207/work
pytz @ file:///C:/b/abs_19q3ljkez4/croot/pytz_1695131651401/work
pyviz_comms @ file:///C:/b/abs_31r9afnand/croot/pyviz_comms_1701728067143/work
pywavelets @ file:///C:/b/abs_7est386xsb/croot/pywavelets_1705049855879/work
pywin32==305.1
pywin32-ctypes @ file:///C:/ci_311/pywin32-ctypes_1676427747089/work
pywinpty @ file:///C:/ci_311/pywinpty_1677707791185/work/target/wheels/pywinpty-2.0.10-cp311-none-win_amd64.whl
PyYAML @ file:///C:/b/abs_782o3mbw7z/croot/pyyaml_1698096085010/work
pyzmq @ file:///C:/b/abs_89aq69t0up/croot/pyzmq_1705605705281/work
QDarkStyle @ file:///tmp/build/80754af9/qdarkstyle_1617386714626/work
qstylizer @ file:///C:/ci_311/qstylizer_1678502012152/work/dist/qstylizer-0.2.2-py2.py3-none-any.whl
QtAwesome @ file:///C:/ci_311/qtawesome_1678402331535/work
qtconsole @ file:///C:/b/abs_eb4u9jg07y/croot/qtconsole_1681402843494/work
QtPy @ file:///C:/b/abs_derqu__3p8/croot/qtpy_1700144907661/work
queuelib @ file:///C:/b/abs_563lpxcne9/croot/queuelib_1696951148213/work
referencing @ file:///C:/b/abs_09f4hj6adf/croot/referencing_1699012097448/work
regex @ file:///C:/b/abs_d5e2e5uqmr/croot/regex_1696515472506/work
requests @ file:///C:/b/abs_474vaa3x9e/croot/requests_1707355619957/work
requests-file @ file:///Users/ktietz/demo/mc3/conda-bld/requests-file_1629455781986/work
requests-toolbelt @ file:///C:/b/abs_2fsmts66wp/croot/requests-toolbelt_1690874051210/work
rfc3339-validator @ file:///C:/b/abs_ddfmseb_vm/croot/rfc3339-validator_1683077054906/work
rfc3986-validator @ file:///C:/b/abs_6e9azihr8o/croot/rfc3986-validator_1683059049737/work
rich @ file:///C:/b/abs_09j2g5qnu8/croot/rich_1684282185530/work
rope @ file:///C:/ci_311/rope_1678402524346/work
rpds-py @ file:///C:/b/abs_76j4g4la23/croot/rpds-py_1698947348047/work
Rtree @ file:///C:/ci_311/rtree_1676455758391/work
ruamel-yaml-conda @ file:///C:/ci_311/ruamel_yaml_1676455799258/work
ruamel.yaml @ file:///C:/ci_311/ruamel.yaml_1676439214109/work
s3fs @ file:///C:/b/abs_24vbfcawyu/croot/s3fs_1701294224436/work
scikit-image @ file:///C:/b/abs_f7z1pjjn6f/croot/scikit-image_1707346180040/work
scikit-learn @ file:///C:/b/abs_38k7ridbgr/croot/scikit-learn_1684954723009/work
scipy==1.11.4
Scrapy @ file:///C:/ci_311/scrapy_1678502587780/work
seaborn @ file:///C:/ci_311/seaborn_1676446547861/work
semver @ file:///tmp/build/80754af9/semver_1603822362442/work
Send2Trash @ file:///C:/b/abs_08dh49ew26/croot/send2trash_1699371173324/work
service-identity @ file:///Users/ktietz/demo/mc3/conda-bld/service_identity_1629460757137/work
sip @ file:///C:/b/abs_edevan3fce/croot/sip_1698675983372/work
six @ file:///tmp/build/80754af9/six_1644875935023/work
smart-open @ file:///C:/ci_311/smart_open_1676439339434/work
smmap @ file:///tmp/build/80754af9/smmap_1611694433573/work
sniffio @ file:///C:/b/abs_3akdewudo_/croot/sniffio_1705431337396/work
snowballstemmer @ file:///tmp/build/80754af9/snowballstemmer_1637937080595/work
sortedcontainers @ file:///tmp/build/80754af9/sortedcontainers_1623949099177/work
soupsieve @ file:///C:/b/abs_bbsvy9t4pl/croot/soupsieve_1696347611357/work
Sphinx @ file:///C:/ci_311/sphinx_1676434546244/work
sphinxcontrib-applehelp @ file:///home/ktietz/src/ci/sphinxcontrib-applehelp_1611920841464/work
sphinxcontrib-devhelp @ file:///home/ktietz/src/ci/sphinxcontrib-devhelp_1611920923094/work
sphinxcontrib-htmlhelp @ file:///tmp/build/80754af9/sphinxcontrib-htmlhelp_1623945626792/work
sphinxcontrib-jsmath @ file:///home/ktietz/src/ci/sphinxcontrib-jsmath_1611920942228/work
sphinxcontrib-qthelp @ file:///home/ktietz/src/ci/sphinxcontrib-qthelp_1611921055322/work
sphinxcontrib-serializinghtml @ file:///tmp/build/80754af9/sphinxcontrib-serializinghtml_1624451540180/work
spyder @ file:///C:/b/abs_e99kl7d8t0/croot/spyder_1681934304813/work
spyder-kernels @ file:///C:/b/abs_e788a8_4y9/croot/spyder-kernels_1691599588437/work
SQLAlchemy @ file:///C:/b/abs_876dxwqqu8/croot/sqlalchemy_1705089154696/work
stack-data @ file:///opt/conda/conda-bld/stack_data_1646927590127/work
statsmodels @ file:///C:/b/abs_7bth810rna/croot/statsmodels_1689937298619/work
streamlit @ file:///C:/b/abs_ba5je7xxy7/croot/streamlit_1706200559831/work
sympy @ file:///C:/b/abs_82njkonm7f/croot/sympy_1701397685028/work
tables @ file:///C:/b/abs_411740ajo7/croot/pytables_1705614883108/work
tabulate @ file:///C:/b/abs_21rf8iibnh/croot/tabulate_1701354830521/work
tblib @ file:///Users/ktietz/demo/mc3/conda-bld/tblib_1629402031467/work
tenacity @ file:///C:/b/abs_ddkoa9nju6/croot/tenacity_1682972298929/work
terminado @ file:///C:/ci_311/terminado_1678228513830/work
text-unidecode @ file:///Users/ktietz/demo/mc3/conda-bld/text-unidecode_1629401354553/work
textdistance @ file:///tmp/build/80754af9/textdistance_1612461398012/work
threadpoolctl @ file:///Users/ktietz/demo/mc3/conda-bld/threadpoolctl_1629802263681/work
three-merge @ file:///tmp/build/80754af9/three-merge_1607553261110/work
tifffile @ file:///C:/b/abs_45o5chuqwt/croot/tifffile_1695107511025/work
tinycss2 @ file:///C:/ci_311/tinycss2_1676425376744/work
tldextract @ file:///opt/conda/conda-bld/tldextract_1646638314385/work
toml @ file:///tmp/build/80754af9/toml_1616166611790/work
tomlkit @ file:///C:/ci_311/tomlkit_1676425418821/work
toolz @ file:///C:/ci_311/toolz_1676431406517/work
tornado @ file:///C:/b/abs_0cbrstidzg/croot/tornado_1696937003724/work
tqdm @ file:///C:/b/abs_f76j9hg7pv/croot/tqdm_1679561871187/work
traitlets @ file:///C:/ci_311/traitlets_1676423290727/work
truststore @ file:///C:/b/abs_55z7b3r045/croot/truststore_1695245455435/work
Twisted @ file:///C:/b/abs_e7yqd811in/croot/twisted_1708702883769/work
twisted-iocpsupport @ file:///C:/ci_311/twisted-iocpsupport_1676447612160/work
typing_extensions @ file:///C:/b/abs_72cdotwc_6/croot/typing_extensions_1705599364138/work
tzdata @ file:///croot/python-tzdata_1690578112552/work
tzlocal @ file:///C:/ci_311/tzlocal_1676439620276/work
uc-micro-py @ file:///C:/ci_311/uc-micro-py_1676457695423/work
ujson @ file:///C:/ci_311/ujson_1676434714224/work
Unidecode @ file:///tmp/build/80754af9/unidecode_1614712377438/work
urllib3 @ file:///C:/b/abs_0c3739ssy1/croot/urllib3_1707349314852/work
validators @ file:///tmp/build/80754af9/validators_1612286467315/work
w3lib @ file:///C:/b/abs_957begrwnl/croot/w3lib_1708640020760/work
watchdog @ file:///C:/ci_311/watchdog_1676457923624/work
wcwidth @ file:///Users/ktietz/demo/mc3/conda-bld/wcwidth_1629357192024/work
webencodings==0.5.1
websocket-client @ file:///C:/ci_311/websocket-client_1676426063281/work
Werkzeug @ file:///C:/b/abs_8578rs2ra_/croot/werkzeug_1679489759009/work
whatthepatch @ file:///C:/ci_311/whatthepatch_1678402578113/work
widgetsnbextension @ file:///C:/b/abs_derxhz1biv/croot/widgetsnbextension_1701273671518/work
win-inet-pton @ file:///C:/ci_311/win_inet_pton_1676425458225/work
wrapt @ file:///C:/ci_311/wrapt_1676432805090/work
xarray @ file:///C:/b/abs_5bkjiynp4e/croot/xarray_1689041498548/work
xlwings @ file:///C:/ci_311_rebuilds/xlwings_1679013429160/work
xyzservices @ file:///C:/ci_311/xyzservices_1676434829315/work
yapf @ file:///tmp/build/80754af9/yapf_1615749224965/work
yarl @ file:///C:/b/abs_8bxwdyhjvp/croot/yarl_1701105248152/work
zict @ file:///C:/b/abs_780gyydtbp/croot/zict_1695832899404/work
zipp @ file:///C:/b/abs_b0beoc27oa/croot/zipp_1704206963359/work
zope.interface @ file:///C:/ci_311/zope.interface_1676439868776/work
zstandard==0.19.0





