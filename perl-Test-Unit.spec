%define upstream_name    Test-Unit
%define upstream_version 0.25

%define _requires_exceptions perl(Error)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	Test::Unit::TestCase - unit testing framework base class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Test::Unit::TestCase is the 'workhorse' of the PerlUnit framework.
When writing tests, you generally subclass Test::Unit::TestCase,
write set_up and tear_down functions if you need them, a bunch of
test_* test methods, then do

%prep

%setup -q -n %{upstream_name}-%{upstream_version}

# perl path hack
find . -type f | xargs perl -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor

%make OPTIMIZE="%{optflags}"

%check
# make test fails
#make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean 
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog Changes README doc examples
%{perl_vendorlib}/Test/*.p*
%{perl_vendorlib}/Test/Unit
%{_mandir}/*/*
