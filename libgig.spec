#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	C++ library for loading, modifying and creating sample files
Name:		libgig
Version:	4.1.0
Release:	1
License:	LGPL + GPL v2
Group:		Libraries
Source0:	http://download.linuxsampler.org/packages/%{name}-%{version}.tar.bz2
# Source0-md5:	a2ad3f933d13332b7a2ea68de20fa4b7
URL:		https://www.linuxsampler.org/libgig/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libsndfile >= 1.0.2
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgig is a C++ library for loading, modifying existing and creating
new Gigasampler (.gig) files and DLS (Downloadable Sounds) Level 1/2
files, KORG sample based instruments (.KSF and .KMP files), SoundFont
v2 (.sf2) files and AKAI sampler data.

%package tools
Summary:	libgig tools
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description tools
This package provides sample file processing tools provided with the
libgig library.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%package static
Summary:	Static %{name} library
Summary(pl.UTF-8):	Statyczna biblioteka %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} library.

%description static -l pl.UTF-8
Statyczna biblioteka %{name}.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make} \
	pkglibdir="%{_libdir}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	pkglibdir="%{_libdir}" \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libgig.so.8.*.*
%attr(755,root,root) %ghost %{_libdir}/libgig.so.8
%attr(755,root,root) %{_libdir}/libakai.so.0.*.*
%attr(755,root,root) %ghost %{_libdir}/libakai.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgig.so
%attr(755,root,root) %{_libdir}/libakai.so
%{_includedir}/%{name}
%{_pkgconfigdir}/akai.pc
%{_pkgconfigdir}/gig.pc

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akaidump
%attr(755,root,root) %{_bindir}/akaiextract
%attr(755,root,root) %{_bindir}/dlsdump
%attr(755,root,root) %{_bindir}/gig2mono
%attr(755,root,root) %{_bindir}/gig2stereo
%attr(755,root,root) %{_bindir}/gigdump
%attr(755,root,root) %{_bindir}/gigextract
%attr(755,root,root) %{_bindir}/gigmerge
%attr(755,root,root) %{_bindir}/korg2gig
%attr(755,root,root) %{_bindir}/korgdump
%attr(755,root,root) %{_bindir}/rifftree
%attr(755,root,root) %{_bindir}/sf2dump
%attr(755,root,root) %{_bindir}/sf2extract
%{_mandir}/man1/akaidump.1*
%{_mandir}/man1/akaiextract.1*
%{_mandir}/man1/dlsdump.1*
%{_mandir}/man1/gig2mono.1*
%{_mandir}/man1/gig2stereo.1*
%{_mandir}/man1/gigdump.1*
%{_mandir}/man1/gigextract.1*
%{_mandir}/man1/gigmerge.1*
%{_mandir}/man1/korg2gig.1*
%{_mandir}/man1/korgdump.1*
%{_mandir}/man1/rifftree.1*
%{_mandir}/man1/sf2dump.1*
%{_mandir}/man1/sf2extract.1*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgig.a
%{_libdir}/libakai.a
%endif
