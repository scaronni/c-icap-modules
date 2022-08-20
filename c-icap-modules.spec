Summary:    Services for the c-icap server
Name:       c-icap-modules
Version:    0.5.5
Release:    2%{?dist}
License:    LGPLv2+
URL:        http://c-icap.sourceforge.net/

Source0:    http://downloads.sourceforge.net/project/c-icap/%{name}/0.5.x/c_icap_modules-%{version}.tar.gz

BuildRequires:  bzip2-devel
BuildRequires:  c-icap-devel >= %{version}
BuildRequires:  clamav-devel
BuildRequires:  gcc
BuildRequires:  libdb-devel
BuildRequires:  make

Requires:   c-icap >= %{version}

%description
C-icap is an implementation of an ICAP server. It can be used with HTTP proxies
that support the ICAP protocol to implement content adaptation and filtering
services. Most of the commercial HTTP proxies must support the ICAP protocol,
the open source Squid 3.x proxy server supports it too.

Currently the following services have been implemented for the c-icap server:
  - virus_scan, an antivirus ICAP service
  - url_check, an URL blacklist/whitelist icap service
  - srv_content_filtering, a score based content filtering icap service

%prep
%autosetup -n c_icap_modules-%{version}

%build
%configure \
  --disable-static \
  --enable-shared \
  --enable-virus_scan-profiles \
  --with-clamav \
  --with-bdb

%make_build

%install
mkdir -p %{buildroot}%{_sysconfdir}/c-icap

%make_install

rm -f %{buildroot}%{_libdir}/c_icap/*.la

# Do not add default configuration files
rm -f %{buildroot}%{_sysconfdir}/c-icap/*.default

%files
%license COPYING
%attr(640,root,c-icap) %config(noreplace) %{_sysconfdir}/c-icap/*.conf
%{_bindir}/c-icap-mods-sguardDB
%{_libdir}/c_icap/clamav_mod.so
%{_libdir}/c_icap/clamd_mod.so
%{_libdir}/c_icap/srv_content_filtering.so
%{_libdir}/c_icap/srv_url_check.so
%{_libdir}/c_icap/virus_scan.so
%{_datadir}/c_icap/templates/srv_content_filtering/en/BLOCK
%{_datadir}/c_icap/templates/srv_url_check/en/DENY
%{_datadir}/c_icap/templates/virus_scan/en/VIRUS_FOUND
%{_datadir}/c_icap/templates/virus_scan/en/VIR_MODE_HEAD
%{_datadir}/c_icap/templates/virus_scan/en/VIR_MODE_PROGRESS
%{_datadir}/c_icap/templates/virus_scan/en/VIR_MODE_TAIL
%{_datadir}/c_icap/templates/virus_scan/en/VIR_MODE_VIRUS_FOUND
%{_datadir}/man/man8/c-icap-mods-sguardDB.8.gz

%changelog
* Sat Aug 20 2022 Simone Caronni <negativo17@gmail.com> - 0.5.5-2
- Clean up SPEC file, use packaging guidelines where possible and fix rpmlint
  issues.
- Trim changelog.
- Do not add default configuration files to configuration directory.

* Fri Mar 19 2021 Frank Crawford <frank@crawford.emu.id.au> - 0.5.5-1
- Update to 0.5.5

* Sun Mar 14 2021 Frank Crawford <frank@crawford.emu.id.au> - 0.5.4-1
- Update to 0.5.4
