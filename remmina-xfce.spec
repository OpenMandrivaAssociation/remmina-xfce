Summary:	Xfce panel plugin for remmina
Name:		remmina-xfce
Version:	0.8.1
Release:	%mkrel 2
License:	GPLv2
Group:		Graphical desktop/Xfce
Url:		http://remmina.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/remmina/%{version}/%{name}-%{version}.tar.gz
Requires:	remmina >= %{version}-%{release}
BuildRequires:	libxfce4util-devel >= 4.3.99.2
BuildRequires:	libxfce4-panel-devel >= 4.3.99.2
BuildRequires:	avahi-client-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	perl(XML::Parser)
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Remmina is a remote desktop client written in GTK+, aiming to be
useful for system administrators and travellers, who need to work with
lots of remote computers in front of either large monitors or tiny
netbooks. Remmina supports multiple network protocols in an integrated
and consistant user interface. Currently RDP, VNC, XDMCP and SSH are
supported.

This package contains an Xfce panel plugin for remmina.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%_libdir/xfce4/panel-plugins/*.*
%_datadir/xfce4/panel-plugins/remmina-xfce-plugin.desktop
%_datadir/locale/*/*/remmina-xfce.mo


%changelog
* Fri Apr 29 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8.1-2mdv2011.0
+ Revision: 660729
- rebuild

* Sat Sep 04 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8.1-1mdv2011.0
+ Revision: 575892
- update to new version 0.8.1

* Sat Jul 17 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8.0-1mdv2011.0
+ Revision: 554538
- update to new version 0.8.0
- spec file clean

* Tue Jul 13 2010 Lev Givon <lev@mandriva.org> 0.7.3-1mdv2011.0
+ Revision: 551388
- import remmina-xfce

