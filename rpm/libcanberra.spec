Name:    libcanberra
Version: 0.30
Release: 1
Summary: Portable Sound Event Library
Group:   System Environment/Libraries
Source0: http://0pointer.de/lennart/projects/libcanberra/libcanberra-%{version}.tar.xz
Patch0:  fix-automake.patch

License: LGPLv2+
Url:     http://git.0pointer.de/?p=libcanberra.git;a=summary
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(vorbis)
BuildRequires: libtool-ltdl-devel
BuildRequires: pkgconfig(libpulse) >= 0.9.15
BuildRequires: gettext-devel
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(systemd)
Requires: sound-theme-freedesktop
Requires: pulseaudio >= 0.9.15
Requires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
A small and lightweight implementation of the XDG Sound Theme Specification
(http://0pointer.de/public/sound-theme-spec.html).

%package  devel
Summary:  Development Files for libcanberra Client Development
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Development Files for libcanberra Client Development

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%prep
%setup -q -n %{name}-%{version}/%{name}

%patch0 -p1

%build
%autogen 
%configure --disable-static --enable-pulse --disable-alsa --enable-null --disable-gstreamer --disable-oss --disable-tdb --disable-gtk --disable-gtk3

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}/%{_datadir}/vala

%files
%defattr(-,root,root)
%doc LGPL
%{_libdir}/libcanberra.so.*
%dir %{_libdir}/libcanberra-%{version}
%{_libdir}/libcanberra-%{version}/libcanberra-pulse.so
%{_libdir}/libcanberra-%{version}/libcanberra-null.so
%{_libdir}/libcanberra-%{version}/libcanberra-multi.so
#%{_docdir}/libcanberra/README

%files devel
%defattr(-,root,root)
%{_includedir}/canberra.h
%{_libdir}/libcanberra.so
%{_libdir}/pkgconfig/libcanberra.pc
#%{_datadir}/gtk-doc/html/libcanberra/
