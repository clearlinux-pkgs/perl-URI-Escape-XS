#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-URI-Escape-XS
Version  : 0.14
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/D/DA/DANKOGAI/URI-Escape-XS-0.14.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DANKOGAI/URI-Escape-XS-0.14.tar.gz
Summary  : 'Drop-In replacement for URI::Escape'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-URI-Escape-XS-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
URI::Escape::XS - Drop-In replacement for URI::Escape
VERSION
SYNOPSIS
# use it instead of URI::Escape
use URI::Escape::XS qw/uri_escape uri_unescape/;
$safe = uri_escape("10% is enough\n");
$verysafe = uri_escape("foo", "\0-\377");
$str  = uri_unescape($safe);

%package dev
Summary: dev components for the perl-URI-Escape-XS package.
Group: Development
Provides: perl-URI-Escape-XS-devel = %{version}-%{release}
Requires: perl-URI-Escape-XS = %{version}-%{release}

%description dev
dev components for the perl-URI-Escape-XS package.


%package perl
Summary: perl components for the perl-URI-Escape-XS package.
Group: Default
Requires: perl-URI-Escape-XS = %{version}-%{release}

%description perl
perl components for the perl-URI-Escape-XS package.


%prep
%setup -q -n URI-Escape-XS-0.14
cd %{_builddir}/URI-Escape-XS-0.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/URI::Escape::XS.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
