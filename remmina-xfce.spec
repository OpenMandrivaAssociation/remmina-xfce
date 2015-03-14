Summary:	Xfce panel plugin for remmina
Name:		remmina-xfce
Version:	0.8.1
Release:	4
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
%configure
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
