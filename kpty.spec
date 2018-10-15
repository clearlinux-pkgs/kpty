#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kpty
Version  : 5.51.0
Release  : 5
URL      : https://download.kde.org/stable/frameworks/5.51/kpty-5.51.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.51/kpty-5.51.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.51/kpty-5.51.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: kpty-lib = %{version}-%{release}
Requires: kpty-license = %{version}-%{release}
Requires: kpty-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

%description
# KPty
Interfacing with pseudo terminal devices
## Introduction
This library provides primitives to interface with pseudo terminal devices
as well as a KProcess derived class for running child processes and
communicating with them using a pty.

%package dev
Summary: dev components for the kpty package.
Group: Development
Requires: kpty-lib = %{version}-%{release}
Provides: kpty-devel = %{version}-%{release}

%description dev
dev components for the kpty package.


%package lib
Summary: lib components for the kpty package.
Group: Libraries
Requires: kpty-license = %{version}-%{release}

%description lib
lib components for the kpty package.


%package license
Summary: license components for the kpty package.
Group: Default

%description license
license components for the kpty package.


%package locales
Summary: locales components for the kpty package.
Group: Default

%description locales
locales components for the kpty package.


%prep
%setup -q -n kpty-5.51.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539617526
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1539617526
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kpty
cp COPYING %{buildroot}/usr/share/package-licenses/kpty/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kpty/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang kpty5

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KPty/KPty
/usr/include/KF5/KPty/KPtyDevice
/usr/include/KF5/KPty/KPtyProcess
/usr/include/KF5/KPty/kpty.h
/usr/include/KF5/KPty/kpty_export.h
/usr/include/KF5/KPty/kptydevice.h
/usr/include/KF5/KPty/kptyprocess.h
/usr/include/KF5/kpty_version.h
/usr/lib64/cmake/KF5Pty/KF5PtyConfig.cmake
/usr/lib64/cmake/KF5Pty/KF5PtyConfigVersion.cmake
/usr/lib64/cmake/KF5Pty/KF5PtyTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Pty/KF5PtyTargets.cmake
/usr/lib64/libKF5Pty.so
/usr/lib64/qt5/mkspecs/modules/qt_KPty.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Pty.so.5
/usr/lib64/libKF5Pty.so.5.51.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kpty/COPYING
/usr/share/package-licenses/kpty/COPYING.LIB

%files locales -f kpty5.lang
%defattr(-,root,root,-)

