#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	List
%define		pnam	Member
Summary:	List::Member - PROLOG's member/2: return index of $x in @y
Summary(pl):	List::Member - member/2 z PROLOGa: zwraca indeks $x w @y
Name:		perl-List-Member
Version:	0.02
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4ed9526901ff53977bc7d3ff0e3f0bf9
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tiny routine to achieve the same effect as PROLOG's "member/2".

Returns the index of supplied scalar in supplied array, or returns the
value of the package's "$NEG" scalar. This can be over-riden for the
case when the target is the same as the default "-1".

%description -l pl
Jest to ma�a funkcja napisana tak, by dawa� taki sam efekt jak
"member/2" z PROLOGa. Zwraca indeks podanej liczby w podanej tablicy
lub zwraca warto�� liczby "$NEG" z pakietu. Ta liczba mo�e by�
nadpisana na wypadek, gdyby poszukiwana liczba by�a taka sama, jak
domy�lna $NEG, czyli -1.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests: %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
