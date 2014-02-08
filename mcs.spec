%define oname	libmcs
%define major	1
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname -d %{name}

Summary:	Modular Config System
Name:		mcs
Version:	0.7.2
Release:	4
License:	BSD
Group:		System/Libraries
Url:		http://www.atheme.org/projects/mcs.shtml
Source0:	http://distfiles.atheme.org/%{oname}-%{version}.tbz2
Patch0:		libmcs-0.7.1-linking.patch
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(libmowgli)

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
Suggests:	%{name} >= %{version}-%{release}

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{devname}
Group:		Development/C
Summary:	Modular Config System shared library
Requires:	%{libname} = %{version}-%{release}
Provides:	libmcs-devel = %{version}-%{release}

%description -n %{devname}
This package includes the development files for %{name}.

%package gconf
Group:		System/Libraries
Summary:	Modular Config System - GConf backend
Requires:	%{name} = %{version}-%{release}

%description gconf
The GConf module for %{name}.

%prep
%setup -qn %{oname}-%{version}
%apply_patches

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

%files -n %{devname}
%{_libdir}/libmcs.so
%{_libdir}/pkgconfig/libmcs.pc
%{_includedir}/libmcs/

