%include	/usr/lib/rpm/macros.perl
%define		pdir	List
%define		pnam	Member
Summary:	List::Member - PROLOG's member/2: return index of $x in @y
Summary(pl):	List::Member - member/2 z PROLOGa: zwraca indeks $x w @y
Name:		perl-List-Member
Version:	0.02
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tiny routine to achieve the same effect as PROLOG's "member/2".

Returns the index of supplied scalar in supplied array, or returns the
value of the package's "$NEG" scalar. This can be over-riden for the
case when the target is the same as the default "-1".

%description -l pl
Jest to ma³a funkcja napisana tak, by dawaæ taki sam efekt jak
"member/2" z PROLOGa. Zwraca indeks podanej liczby w podanej tablicy
lub zwraca warto¶æ liczby "$NEG" z pakietu. Ta liczba mo¿e byæ
nadpisana na wypadek, gdyby poszukiwana liczba by³a taka sama, jak
domy¶lna $NEG, czyli -1.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
#%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
