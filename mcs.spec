%define name mcs
%define version 0.7.1
%define release %mkrel 4
%define oname libmcs

%define major 1
%define libname %mklibname %name %major
%define develname %mklibname -d %name

Summary: Modular Config System
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://distfiles.atheme.org/%{oname}-%{version}.tbz2
Patch: libmcs-0.7.1-linking.patch
License: BSD
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url: http://www.atheme.org/projects/mcs.shtml
BuildRequires: libmowgli-devel
BuildRequires: libGConf2-devel

%description
mcs is a library and set of userland tools which abstract the storage
of configuration settings away from userland applications.

It is hoped that by using mcs, that the applications which use it will
generally have a more congruent feeling in regards to settings.

There have been other projects like this before (such as GConf), but
unlike those projects, mcs strictly handles abstraction. It does not
impose any specific data storage requirement, nor is it tied to any
desktop environment or software suite.

%package -n %libname
Group: System/Libraries
Summary: Modular Config System shared library
Requires: %name >= %version

%description -n %libname
mcs is a library and set of userland tools which abstract the storage
of configuration settings away from userland applications.

It is hoped that by using mcs, that the applications which use it will
generally have a more congruent feeling in regards to settings.

There have been other projects like this before (such as GConf), but
unlike those projects, mcs strictly handles abstraction. It does not
impose any specific data storage requirement, nor is it tied to any
desktop environment or software suite.

%package -n %develname
Group: Development/C
Summary: Modular Config System shared library
Requires: %libname = %version
Provides: libmcs-devel = %version-%release
Obsoletes: %mklibname -d %name 1

%description -n %develname
mcs is a library and set of userland tools which abstract the storage
of configuration settings away from userland applications.

It is hoped that by using mcs, that the applications which use it will
generally have a more congruent feeling in regards to settings.

There have been other projects like this before (such as GConf), but
unlike those projects, mcs strictly handles abstraction. It does not
impose any specific data storage requirement, nor is it tied to any
desktop environment or software suite.

%package gconf
Group: System/Libraries
Summary: Modular Config System - GConf backend
Requires: %name = %version

%description gconf
mcs is a library and set of userland tools which abstract the storage
of configuration settings away from userland applications.

It is hoped that by using mcs, that the applications which use it will
generally have a more congruent feeling in regards to settings.

There have been other projects like this before (such as GConf), but
unlike those projects, mcs strictly handles abstraction. It does not
impose any specific data storage requirement, nor is it tied to any
desktop environment or software suite.

%prep
%setup -q -n %oname-%version
%patch -p1 -b .linking

%build
%configure2_5x --disable-kconfig
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS TODO README
%_bindir/mcs-*
%dir %_libdir/mcs/
%_libdir/mcs/keyfile.so

%files gconf
%defattr(-,root,root)
%_libdir/mcs/gconf.so

%files -n %libname
%defattr(-,root,root)
%_libdir/libmcs.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%_libdir/libmcs.so
%_libdir/pkgconfig/libmcs.pc
%_includedir/libmcs/


