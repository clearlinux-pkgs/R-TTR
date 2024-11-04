#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v2
# autospec commit: e661f3a
#
Name     : R-TTR
Version  : 0.24.4
Release  : 69
URL      : https://cran.r-project.org/src/contrib/TTR_0.24.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/TTR_0.24.4.tar.gz
Summary  : Technical Trading Rules
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-TTR-lib = %{version}-%{release}
Requires: R-curl
Requires: R-xts
Requires: R-zoo
BuildRequires : R-curl
BuildRequires : R-xts
BuildRequires : R-zoo
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
### About
TTR is an [R](https://www.r-project.org) package that provides the most popular
technical analysis functions for financial market data. Many of these functions
are used as components of systematic trading strategies and financial charts.

%package lib
Summary: lib components for the R-TTR package.
Group: Libraries

%description lib
lib components for the R-TTR package.


%prep
%setup -q -n TTR
pushd ..
cp -a TTR buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701167666

%install
export SOURCE_DATE_EPOCH=1701167666
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/TTR/DESCRIPTION
/usr/lib64/R/library/TTR/INDEX
/usr/lib64/R/library/TTR/Meta/Rd.rds
/usr/lib64/R/library/TTR/Meta/data.rds
/usr/lib64/R/library/TTR/Meta/features.rds
/usr/lib64/R/library/TTR/Meta/hsearch.rds
/usr/lib64/R/library/TTR/Meta/links.rds
/usr/lib64/R/library/TTR/Meta/nsInfo.rds
/usr/lib64/R/library/TTR/Meta/package.rds
/usr/lib64/R/library/TTR/NAMESPACE
/usr/lib64/R/library/TTR/NEWS.md
/usr/lib64/R/library/TTR/R/TTR
/usr/lib64/R/library/TTR/R/TTR.rdb
/usr/lib64/R/library/TTR/R/TTR.rdx
/usr/lib64/R/library/TTR/data/ttrc.rda
/usr/lib64/R/library/TTR/help/AnIndex
/usr/lib64/R/library/TTR/help/TTR.rdb
/usr/lib64/R/library/TTR/help/TTR.rdx
/usr/lib64/R/library/TTR/help/aliases.rds
/usr/lib64/R/library/TTR/help/paths.rds
/usr/lib64/R/library/TTR/html/00Index.html
/usr/lib64/R/library/TTR/html/R.css
/usr/lib64/R/library/TTR/tests/doRUnit.R
/usr/lib64/R/library/TTR/unitTests/output.MA.rda
/usr/lib64/R/library/TTR/unitTests/output.Oscillators.rda
/usr/lib64/R/library/TTR/unitTests/output.misc.rda
/usr/lib64/R/library/TTR/unitTests/output.overlays.rda
/usr/lib64/R/library/TTR/unitTests/output.runFun.rda
/usr/lib64/R/library/TTR/unitTests/output.trend.rda
/usr/lib64/R/library/TTR/unitTests/output.volatility.rda
/usr/lib64/R/library/TTR/unitTests/output.volume.rda
/usr/lib64/R/library/TTR/unitTests/runit.TTR.DVI.R
/usr/lib64/R/library/TTR/unitTests/runit.TTR.Misc.R
/usr/lib64/R/library/TTR/unitTests/runit.TTR.MovingAverages.R
/usr/lib64/R/library/TTR/unitTests/runit.TTR.Oscillators.R
/usr/lib64/R/library/TTR/unitTests/runit.TTR.Overlays.R
/usr/lib64/R/library/TTR/unitTests/runit.TTR.Trend.R
/usr/lib64/R/library/TTR/unitTests/runit.TTR.Volatility.R
/usr/lib64/R/library/TTR/unitTests/runit.TTR.Volume.R
/usr/lib64/R/library/TTR/unitTests/runit.TTR.runFun.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/TTR/libs/TTR.so
/usr/lib64/R/library/TTR/libs/TTR.so.avx2
/usr/lib64/R/library/TTR/libs/TTR.so.avx512
