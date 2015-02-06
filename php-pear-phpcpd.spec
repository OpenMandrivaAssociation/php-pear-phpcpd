%define  upstream_name phpcpd
%define __noautoreq /usr/bin/php

Summary:	Copy/Paste Detector (CPD) for PHP code

Name:		php-pear-%{upstream_name}
Version:	1.3.5
Release:	3
License:	BSD
Group:		Development/PHP
URL:		http://www.phpunit.de/
Source0:	http://pear.phpunit.de/get/phpcpd-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-cli >= 3:5.2.1
Requires:	php-pear >= 1:1.9.4
Requires:	php-channel-phpunit
BuildArch:	noarch
BuildRequires:	php-pear
BuildRequires:	php-channel-phpunit
Suggests:	php-pear-PHPUnit >= 3.6.3
Suggests:	php-pear-File_Iterator >= 1.3.0
Suggests:	php-pear-PHP_Timer >= 1.0.2
Suggests:	php-tokenizer

%description
PHPUnit is a regression testing framework used by the developer who implements
unit tests in PHP.

This package provides Copy/Paste Detector (CPD) for PHP code for PHPUnit.

%prep

%setup -q -c 
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%build

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%{_bindir}/phpcpd
%{_datadir}/pear/PHPCPD
%{_datadir}/pear/packages/phpcpd.xml



