Summary: A customized configuration of the fvwm2 window manager.
Name: AnotherLevel
Version: 0.9
Release: 1
Copyright: distributable
Group: User Interface/Desktops
Source: AnotherLevel-0.9.tar.gz
Requires: m4, fvwm2, fvwm2-icons, wmconfig > 0.3, redhat-logos
BuildArchitectures: noarch
BuildRoot: /var/tmp/AnotherLevel-root
Obsoletes: TheNextLevel

%description 
AnotherLevel is a custom configuration of the popular fvwm2
window manager. Fvwm stands for (?) virtual window manager.
You can fill in the blank for the 'f': fast, flexible, 
friendly and fabulous all could apply. This window manager
is based on TheNextLevel desktop configuration, created
by Greg J. Badros, which won the 1996 Red Hat Desktop 
Contest.

AnotherLevel is designed to be easily configured by the 
user.

%prep
%setup -c -q

%build
echo "No build necessary"

%install
TOPDIR=$RPM_BUILD_ROOT make install
mkdir -p $RPM_BUILD_ROOT/etc/X11/TheNextLevel
ln -sf ../AnotherLevel/fvwm2rc.m4 \
	$RPM_BUILD_ROOT/etc/X11/TheNextLevel/.fvwm2rc.m4

mkdir -p $RPM_BUILD_ROOT/etc/X11/gdm/Sessions
install -m 755 AnotherLevel.session \
	$RPM_BUILD_ROOT/etc/X11/gdm/Sessions/AnotherLevel

%files
%defattr(-,root,root)
%doc Sample.Xmodmap
%dir /etc/X11/AnotherLevel
%config /etc/X11/AnotherLevel/*
/etc/X11/TheNextLevel
/etc/X11/gdm/Sessions/AnotherLevel
/usr/share/icons/*.xpm
/usr/share/icons/mini/*.xpm
/usr/man/*/*
/usr/X11R6/bin/*

%clean
rm -rf $RPM_BUILD_ROOT
