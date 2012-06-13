Name:		double-conversion
Version:	1.1.1
Release:	1%{?dist}
Summary:	Library providing binary-decimal and decimal-binary routines for IEEE doubles.

Group:		Development/Languages
License:	BSD
URL:		http://code.google.com/p/double-conversion
Source0:	http://double-conversion.googlecode.com/files/double-conversion-1.1.1.tar.gz
Source1:	SConstruct.double-conversion
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	scons
Requires: 	libstdc++


%description
Library providing binary-decimal and decimal-binary routines for IEEE doubles.

%package devel
Summary: Library providing binary-decimal and decimal-binary routines for IEEE doubles.
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
Contains header files for developing applications that use the %{name} package.


%prep
%setup -n double-conversion


%build
scons -f %{SOURCE1}


%install
%{__install} -D -m 755 ./libdouble_conversion.a %{buildroot}%{_libdir}/libdouble_conversion.a
%{__install} -D -m 755 ./libdouble_conversion_pic.a %{buildroot}%{_libdir}/libdouble_conversion_pic.a

%{__install} -D -m 755 ./src/double-conversion.h %{buildroot}%{_includedir}/double-conversion/double-conversion.h
%{__install} -D -m 755 ./src/bignum.h %{buildroot}%{_includedir}/double-conversion/bignum.h
%{__install} -D -m 755 ./src/bignum-dtoa.h %{buildroot}%{_includedir}/double-conversion/bignum-dtoa.h
%{__install} -D -m 755 ./src/cached-powers.h %{buildroot}%{_includedir}/double-conversion/cached-powers.h
%{__install} -D -m 755 ./src/diy-fp.h %{buildroot}%{_includedir}/double-conversion/diy-fp.h
%{__install} -D -m 755 ./src/fast-dtoa.h %{buildroot}%{_includedir}/double-conversion/fast-dtoa.h
%{__install} -D -m 755 ./src/fixed-dtoa.h %{buildroot}%{_includedir}/double-conversion/fixed-dtoa.h
%{__install} -D -m 755 ./src/ieee.h %{buildroot}%{_includedir}/double-conversion/ieee.h
%{__install} -D -m 755 ./src/strtod.h %{buildroot}%{_includedir}/double-conversion/strtod.h
%{__install} -D -m 755 ./src/utils.h %{buildroot}%{_includedir}/double-conversion/utils.h


%clean
%{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE README AUTHORS
%{_libdir}/*.a

%files devel
%defattr(-,root,root,-)
%{_includedir}/double-conversion/*.h


%changelog

