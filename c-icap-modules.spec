%define modn c_icap_modules
%define name c-icap-modules
%define ver  0.5.5

Summary         : Services for the c-icap server
Name            : %{name}
Version         : %{ver}
Release         : 1%{?dist}%{?pext}
License         : LGPLv2+
Group           : System Environment/Daemons
URL             : http://c-icap.sourceforge.net/
Source0         : http://downloads.sourceforge.net/project/c-icap/%{name}/0.5.x/%{modn}-%{ver}.tar.gz
Buildroot       : %{_tmppath}/%{name}-%{version}-%{release}-root
Requires        : c-icap >= 0.5.2
BuildRequires   : bzip2-devel, c-icap-devel >= 0.5.2, clamav-devel, libdb-devel, tar
BuildRequires	: gcc make
Vendor          : Tsantilas Christos <chtsanti@users.sourceforge.net>

%description
C-icap is an implementation of an ICAP server. It can be used with HTTP proxies
that support the ICAP protocol to implement content adaptation and filtering
services. This package provides additional service modules for c-icap.

Currently the following services have been implemented for the c-icap server:
- Web antivirus service, using the clamav open-source antivirus engine
- basic URL filtering service

%prep
%setup -q -n %{modn}-%{ver}

%build
%configure \
  LDFLAGS="" \
  CFLAGS="${RPM_OPT_FLAGS} -fno-strict-aliasing -I/usr/include/libdb" \
  --enable-shared                                \
  --with-clamav                                  \
  --with-bdb

%{__make} %{?_smp_mflags}

%install
[ -n "${RPM_BUILD_ROOT}" -a "${RPM_BUILD_ROOT}" != "/" ] && %{__rm} -rf ${RPM_BUILD_ROOT}
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_sysconfdir}/c-icap
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_libdir}/c-icap

%{__make} \
  DESTDIR=${RPM_BUILD_ROOT} \
  install

%{__rm}   -f        ${RPM_BUILD_ROOT}%{_libdir}/c_icap/*.la

%clean
[ -n "${RPM_BUILD_ROOT}" -a "${RPM_BUILD_ROOT}" != "/" ] && %{__rm} -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc COPYING INSTALL
%attr(640,root,c-icap) %config(noreplace) %{_sysconfdir}/c-icap/*.conf
%attr(640,root,c-icap) %{_sysconfdir}/c-icap/*.default
%{_libdir}/c_icap/clamav_mod.so
%{_libdir}/c_icap/clamd_mod.so
%{_libdir}/c_icap/srv_content_filtering.so
%{_libdir}/c_icap/srv_url_check.so
%{_libdir}/c_icap/virus_scan.so
/usr/bin/c-icap-mods-sguardDB
/usr/share/c_icap/templates/srv_content_filtering/en/BLOCK
/usr/share/c_icap/templates/srv_url_check/en/DENY
/usr/share/c_icap/templates/virus_scan/en/VIRUS_FOUND
/usr/share/c_icap/templates/virus_scan/en/VIR_MODE_HEAD
/usr/share/c_icap/templates/virus_scan/en/VIR_MODE_PROGRESS
/usr/share/c_icap/templates/virus_scan/en/VIR_MODE_TAIL
/usr/share/c_icap/templates/virus_scan/en/VIR_MODE_VIRUS_FOUND
/usr/share/man/man8/c-icap-mods-sguardDB.8.gz

%changelog
* Fri Mar 19 2021 Frank Crawford <frank@crawford.emu.id.au> - 0.5.5-1
- Update to 0.5.5

* Sun Mar 14 2021 Frank Crawford <frank@crawford.emu.id.au> - 0.5.4-1
- Update to 0.5.4

* Mon Jan 28 2019 Frank Crawford <frank@crawford.emu.id.au> - 0.5.3-1
- Update to 0.5.3
- Includes official update ofr ClamAV 0.101.X API change

* Sun Jan 13 2019 Frank Crawford <frank@crawford.emu.id.au> - 0.5.2-2
- Updated for ClamAV 0.101.1 API change

* Mon Jan 07 2019 Frank Crawford <frank@crawford.emu.id.au> - 0.5.2-1
- Update to 0.5.2

* Thu Mar 16 2017 Marcin Skarbek <rpm@skarbek.name> - 0.4.4-1
- Update to 0.4.4

* Wed Jan 02 2013 Oliver Seeburger <oliver.seeburger@sundermeier-werkzeugbau.de> - 0.2.4-1
- Update to 0.2.4

* Fri Nov 16 2012 Oliver Seeburger <oliver.seeburger@sundermeier-werkzeugbau.de> - 0.2.3-1
- Update to 0.2.3

* Tue Sep 25 2012 Oliver Seeburger <oliver.seeburger@sundermeier-werkzeugbau.de> - 0.2.2-1
- Update to 0.2.2

* Tue Jul 10 2012 Oliver Seeburger <oliver.seeburger@sundermeier-werkzeugbau.de> - 0.2.1-1
- Initial build for Fedora 17
