# taper
far partire il docker (evantualemnet con docker compose)
```
docker run -it --name taper -v <directori dei dati>:/root/data -v ${PWD}/script:/root/script gmazzitelli/cygno-tape:v1.0.5-cygno
```
mettersi nella directory script e dare il comendo:
```
source oicd-setup.sh
```
se si vuole lascre in backgroud CTR-P CTR-Q

e per ricollegarsi ```docker attach taper```

esempio di comendi gfal su cygno
```
gfal-ls davs://xfer-archive.cr.cnaf.infn.it:8443/cygno
gfal-copy test davs://xfer-archive.cr.cnaf.infn.it:8443/cygno/prova.txt
gfal-rm davs://xfer-archive.cr.cnaf.infn.it:8443/cygno/prova.txt
```
