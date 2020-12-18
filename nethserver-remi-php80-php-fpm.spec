Name: nethserver-remi-php80-php-fpm
Version: 1.0.0
Release: 1%{?dist}
Summary: NethServer remi-php80-php-fpm configuration
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: nethserver-devtools

Requires: php80, php80-php-fpm
Requires: php80-php-bcmath, php80-php-gd, php80-php-imap
Requires: php80-php-ldap, php80-php-enchant, php80-php-mbstring
Requires: php80-php-pdo, php80-php-tidy, php80-php-mysqlnd
Requires: php80-php-soap, php80-php-pgsql
Requires: php80-php-pecl-apcu, php80-php-intl
Requires: php80-php-opcache
# specific dependencies from remi to get same PHP modules list of RH SCL
Requires: php80-php-xml, php80-php-pecl-zip, php80-php-process

%description
Basic support for PHP 80 using SCL of remi repository

%prep
%setup -q

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist


%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update


%changelog
* Fri Dec 18 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- PHP80 SCL from remi  - NethServer/dev#6356

* Mon Dec 07 2020 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.0-1
- Initial release of PHP80 for NethServer
