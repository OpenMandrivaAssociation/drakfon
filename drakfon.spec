%define name drakfon
%define version 0.6
%define release %mkrel 5

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
install -m 644 -D %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
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




%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6-5mdv2011.0
+ Revision: 610274
- rebuild

* Sun May 02 2010 Funda Wang <fwang@mandriva.org> 0.6-4mdv2010.1
+ Revision: 541554
- fix perm of desktop file

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.6-4mdv2010.0
+ Revision: 428339
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.6-3mdv2009.0
+ Revision: 244526
- rebuild
- fix no-buildroot-tag

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.6-1mdv2008.1
+ Revision: 124214
- kill re-definition of %%buildroot on Pixel's request


* Tue Apr 03 2007 Olivier Blin <oblin@mandriva.com> 0.6-1mdv2007.1
+ Revision: 150345
- Import drakfon

