Summary:	A customized configuration of the fvwm2 window manager
Summary(pl):	U¿yteczna konfiguracja zarz±dcy okien fvwm2
Name:		AnotherLevel
Version:	0.9
Release:	3
License:	distributable
Group:		X11/Window Managers
# Source0-md5:	ddeb447d0bf8aeca5bb1cf30878b4d55
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	sed >= 4.0
Requires:	fvwm2
Requires:	fvwm2-icons
Requires:	m4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	TheNextLevel
BuildArch:	noarch

%description
AnotherLevel is a custom configuration of the popular fvwm2 window
manager. Fvwm stands for (?) virtual window manager. You can fill in
the blank for the 'f': fast, flexible, friendly and fabulous all could
apply. This window manager is based on TheNextLevel desktop
configuration, created by Greg J. Badros, which won the 1996 Red Hat
Desktop Contest.

AnotherLevel is designed to be easily configured by the user.

%description -l pl
AnotherLevel jest u¿yteczn± konfiguracj± popularnego zarz±dcy okien,
jakim jest fvwm2. Fvwm oznacza (?) wirtualnego zarz±dcê okien. Zamiast
znaku zapytania mo¿na dopisaæ: szybki, elastyczny, przyjazny i
fantastyczny - wszystko to pasowa³oby do niego. Ten zarz±dca okien
bazuje na konfiguracji pulpitu w stylu TheNextLevel stworzonej przez
Grega J. Bradosa, która wygra³a Red Hat Desktop Contest w 1996 roku.

%prep
%setup -c -q

%install
rm -rf $RPM_BUILD_ROOT

# We need 'pixmaps/mini' path, do not need 'pixmaps/redhat' one
sed -i 's/redhat/mini/' scripts/fvwm2rc.defines.m4

%{__make} install \
	TOPDIR=$RPM_BUILD_ROOT \
	ICONDIR=%{_pixmapsdir} \
	MANDIR=%{_mandir}/man1 \
	BINDIR=%{_bindir}

install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/TheNextLevel
ln -sf ../AnotherLevel/fvwm2rc.m4 \
	$RPM_BUILD_ROOT%{_sysconfdir}/X11/TheNextLevel/.fvwm2rc.m4

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Sample.Xmodmap
%dir %{_sysconfdir}/X11/AnotherLevel
%config %{_sysconfdir}/X11/AnotherLevel/*
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/X11/TheNextLevel
%{_pixmapsdir}/*.xpm
%{_pixmapsdir}/mini/*.xpm
%{_mandir}/man1/*
