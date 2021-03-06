#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-etuples
Version  : 0.3.5
Release  : 7
URL      : https://files.pythonhosted.org/packages/3c/5d/1aa7b9f2e267348abc738f41742e1466a4b7363272ebd61989cc548c3fc8/etuples-0.3.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/3c/5d/1aa7b9f2e267348abc738f41742e1466a4b7363272ebd61989cc548c3fc8/etuples-0.3.5.tar.gz
Summary  : Python S-expression emulation using tuple-like objects.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-etuples-license = %{version}-%{release}
Requires: pypi-etuples-python = %{version}-%{release}
Requires: pypi-etuples-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cons)
BuildRequires : pypi(multipledispatch)

%description
# `etuples`
[![Build Status](https://travis-ci.org/pythological/etuples.svg?branch=master)](https://travis-ci.org/pythological/etuples) [![Coverage Status](https://coveralls.io/repos/github/pythological/etuples/badge.svg?branch=master)](https://coveralls.io/github/pythological/etuples?branch=master) [![PyPI](https://img.shields.io/pypi/v/etuples)](https://pypi.org/project/etuples/)

%package license
Summary: license components for the pypi-etuples package.
Group: Default

%description license
license components for the pypi-etuples package.


%package python
Summary: python components for the pypi-etuples package.
Group: Default
Requires: pypi-etuples-python3 = %{version}-%{release}

%description python
python components for the pypi-etuples package.


%package python3
Summary: python3 components for the pypi-etuples package.
Group: Default
Requires: python3-core
Provides: pypi(etuples)
Requires: pypi(cons)
Requires: pypi(multipledispatch)

%description python3
python3 components for the pypi-etuples package.


%prep
%setup -q -n etuples-0.3.5
cd %{_builddir}/etuples-0.3.5
pushd ..
cp -a etuples-0.3.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656406391
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-etuples
cp %{_builddir}/etuples-0.3.5/LICENSE %{buildroot}/usr/share/package-licenses/pypi-etuples/7bd5743dd22a2d17c5f0ac816ba882247cc025ce
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-etuples/7bd5743dd22a2d17c5f0ac816ba882247cc025ce

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
