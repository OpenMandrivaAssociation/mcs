%define oname libmcs

%define major 1
%define libname %mklibname %name %{major}
%define develname %mklibname -d %{name}

Summary:	Modular Config System
Name:		mcs
Version:	0.7.2
Release:	3
License:	BSD
Group:		System/Libraries
Url:		http://www.atheme.org/projects/mcs.shtml
Source0:	http://distfiles.atheme.org/%{oname}-%{version}.tbz2
Patch:		libmcs-0.7.1-linking.patch
BuildRequires:	pkgconfig(libmowgli)
BuildRequires:	pkgconfig(gconf-2.0)

%description
mcs is a library and set of userland tools which abstract the storage
of configuration settings away from userland applications.

It is hoped that by using mcs, that the applications which use it will
generally have a more congruent feeling in regards to settings.

There have been other projects like this before (such as GConf), but
unlike those projects, mcs strictly handles abstraction. It does not
impose any specific data storage requirement, nor is it tied to any
desktop environment or software suite.

%package -n %{libname}
Group:		System/Libraries
Summary:	Modular Config System shared library
Requires:	%{name} >= %{version}

%description -n %{libname}
mcs is a library and set of userland tools which abstract the storage
of configuration settings away from userland applications.

It is hoped that by using mcs, that the applications which use it will
generally have a more congruent feeling in regards to settings.

There have been other projects like this before (such as GConf), but
unlike those projects, mcs strictly handles abstraction. It does not
impose any specific data storage requirement, nor is it tied to any
desktop environment or software suite.

%package -n %{develname}
Group:		Development/C
Summary:	Modular Config System shared library
Requires:	%{libname} = %{version}-%{release}
Provides:	libmcs-devel = %{version}-%{release}

%description -n %{develname}
mcs is a library and set of userland tools which abstract the storage
of configuration settings away from userland applications.

It is hoped that by using mcs, that the applications which use it will
generally have a more congruent feeling in regards to settings.

There have been other projects like this before (such as GConf), but
unlike those projects, mcs strictly handles abstraction. It does not
impose any specific data storage requirement, nor is it tied to any
desktop environment or software suite.

%package gconf
Group:		System/Libraries
Summary:	Modular Config System - GConf backend
Requires:	%{name} = %{version}-%{release}

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
%setup -q -n %{oname}-%{version}
%patch -p1 -b .linking

%build
%configure2_5x --disable-kconfig
%make

%install
%makeinstall_std

%files
%doc AUTHORS TODO README
%{_bindir}/mcs-*
%dir %{_libdir}/mcs/
%{_libdir}/mcs/keyfile.so

%files gconf
%{_libdir}/mcs/gconf.so

%files -n %{libname}
%{_libdir}/libmcs.so.%{major}*

%files -n %{develname}
%{_libdir}/libmcs.so
%{_libdir}/pkgconfig/libmcs.pc
%{_includedir}/libmcs/




%changelog
* Wed Aug 17 2011 Götz Waschk <waschk@mandriva.org> 0.7.2-2mdv2012.0
+ Revision: 694832
- rebuild

* Mon Aug 16 2010 Götz Waschk <waschk@mandriva.org> 0.7.2-1mdv2011.0
+ Revision: 570283
- new version

* Sat Aug 22 2009 Götz Waschk <waschk@mandriva.org> 0.7.1-4mdv2010.0
+ Revision: 419662
- disable kconfig backend
- readd package still needed by audacious and deleted from svn by someone

  + Antoine Ginies <aginies@mandriva.com>
    - 2009.1 rebuild

* Mon Jul 21 2008 Götz Waschk <waschk@mandriva.org> 0.7.1-2mdv2009.0
+ Revision: 239335
- rebuild

* Thu Jun 12 2008 Götz Waschk <waschk@mandriva.org> 0.7.1-1mdv2009.0
+ Revision: 218382
- fix library path on 64 bit
- new version
- fix linking

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Götz Waschk <waschk@mandriva.org> 0.7.0-1mdv2008.1
+ Revision: 170664
- new version
- add kconfig backend
- split out gconf backend

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Tue Jan 01 2008 Götz Waschk <waschk@mandriva.org> 0.6.0-3mdv2008.1
+ Revision: 140163
- rebuild for new libmowgli

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Götz Waschk <waschk@mandriva.org> 0.6.0-2mdv2008.1
+ Revision: 98477
- rebuild for new libmowgli

* Mon Oct 15 2007 Götz Waschk <waschk@mandriva.org> 0.6.0-1mdv2008.1
+ Revision: 98454
- fix buildrequries
- new version
- new URL
- fix build
- new devel name
- update file list


* Tue Feb 27 2007 Götz Waschk <waschk@mandriva.org> 0.4.1-1mdv2007.0
+ Revision: 126328
- new version
- sacrifice a chicken for the build system
- new version

* Mon Feb 19 2007 Götz Waschk <waschk@mandriva.org> 0.3.3-1mdv2007.1
+ Revision: 122673
- new version
- drop patch

* Mon Feb 19 2007 Götz Waschk <waschk@mandriva.org> 0.3.2-2mdv2007.1
+ Revision: 122667
- fix libdir on x86_64
- Import mcs

* Mon Feb 19 2007 Götz Waschk <waschk@mandriva.org> 0.3.2-1mdv2007.1
- initial package

