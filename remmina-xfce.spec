%define name	remmina-xfce
%define version 0.7.3
%define release %mkrel 1

Summary:	Xfce panel plugin for remmina
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.gz
License:	GPLv2
Group:		Graphical desktop/Xfce
Url:		http://remmina.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	remmina >= %{version}-%{release}
BuildRequires:	libxfce4util-devel >= 4.3.99.2
BuildRequires:	libxfce4-panel-devel >= 4.3.99.2
BuildRequires:	avahi-client-devel

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
%makeinstall

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%_libdir/xfce4/panel-plugins/*.*
%_datadir/xfce4/panel-plugins/remmina-xfce-plugin.desktop
%_datadir/locale/*/*/remmina-xfce.mo

