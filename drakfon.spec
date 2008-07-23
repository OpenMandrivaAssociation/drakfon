%define name drakfon
%define version 0.6
%define release %mkrel 3

Summary:	Install FON firmwares in wireless routers
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
License:	GPL	
Group:		System/Configuration/Networking
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url:		http://fon.com
BuildArch:      noarch

%description
Tool to install FON based firmwares in wireless routers

%prep
%setup -q

%build
%make -C po

%install
rm -rf %{buildroot}
%makeinstall_std -C po
install -D -m 755 %{name} %{buildroot}%{_sbindir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}/firmwares
install -m 644 FONbasic-* %{buildroot}%{_datadir}/%{name}/firmwares
install -d %{buildroot}%{_iconsdir}
install -m 644 FON*.png %{buildroot}%{_iconsdir}
install -D %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%{_sbindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/firmwares/
%{_datadir}/%{name}/firmwares/FONbasic-*
%{_iconsdir}/FON*.png
%{_datadir}/applications/%{name}.desktop


