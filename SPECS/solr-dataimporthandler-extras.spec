%define debug_package %{nil}
%define solr_install_dir %{_javadir}/solr
%define plugin_install_dir %{solr_install_dir}/plugins
%define plugin_name dataimporthandler-extras
%define plugin_source_dir contrib/%{plugin_name}
%define __jar_repack 0

Name:           solr-%{plugin_name}
Version:        8.5.2
Release:        0%{?dist}
Summary:        A distributed, highly available, RESTful search engine

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            http://lucene.apache.org/solr/
Source0:        http://archive.apache.org/dist/lucene/solr/%{version}/solr-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       solr >= %{version}

Provides: %{name}

%description
A distributed, highly available, RESTful search engine

%prep
%setup -q -n solr-%{version}

%build
true

%install
rm -rf $RPM_BUILD_ROOT

%{__mkdir} -p %{buildroot}%{plugin_install_dir}
%{__install} -p -m 755 %{plugin_source_dir}/lib/* %{buildroot}%{plugin_install_dir}
%{__install} -p -m 755 dist/solr-%{plugin_name}-* %{buildroot}%{plugin_install_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{plugin_install_dir}/*

%changelog
* Thu Jul 9 2020 Chris Beer <chris@cbeer.info> - 8.5.2-0
- Update to Solr 8.5.0

* Thu Aug 10 2019 Chris Beer <chris@cbeer.info> - 8.2.0-0
- Update to Solr 8.2.0

* Tue Aug 08 2019 Chris Beer <chris@cbeer.info> - 7.7.2-0
- Update to Solr 7.7.2

* Sat Feb 16 2019 Chris Beer <chris@cbeer.info> - 7.7.0-0
- Update to Solr 7.7.0

* Mon Dec 17 2018 Chris Beer <chris@cbeer.info> - 7.6.0-0
- Update to Solr 7.6.0

* Sat Sep 24 2018 Chris Beer <chris@cbeer.info> - 7.5.0-0
- Update to Solr 7.5.0

* Sat Aug 4 2018 Chris Beer <chris@cbeer.info> - 7.4.0-0
- Update to Solr 7.4.0

* Sat Aug 4 2018 Chris Beer <chris@cbeer.info> - 6.6.5-0
- Update to Solr 6.6.5

* Thu Jul 26 2018 Chris Beer <chris@cbeer.info> - 6.6.1-0
- Update to Solr 6.6.1

* Wed Jul 5 2017 Chris Beer <chris@cbeer.info> - 6.6.0-0
- Update to Solr 6.6.0

* Wed May 24 2017 Chris Beer <chris@cbeer.info> - 6.5.1-0
- Update to Solr 6.5.1

* Sun Aug 27 2016 Chris Beer <chris@cbeer.info> - 6.5.1-0
- Update to Solr 6.2.0

* Wed Jun 29 2016 Chris Beer <chris@cbeer.info> - 6.1.0-0
- Update to Solr 6.1.0

* Sat Apr 9 2016 Chris Beer <chris@cbeer.info> - 6.0.0-0
- Update to Solr 6.0.0

* Fri Apr 1 2016 Erin Fahy <efahy@stanford.edu> - 5.4.1-1
- Fix for logrotate and drop the console log

* Mon Jan 25 2016 Chris Beer <chris@cbeer.info> - 5.4.1-0
- Update to Solr 5.4.1

* Tue Dec 15 2015 Chris Beer <chris@cbeer.info> - 5.4.0-0
- Update to Solr 5.4.0

* Sat Sep 26 2015 Chris Beer <chris@cbeer.info> - 5.3.1-0
- Update to Solr 5.3.1

* Thu Sep 10 2015 Chris Beer <chris@cbeer.info> - 5.3.0-1
- Update to Solr 5.3.0

* Tue Jun 2 2015 Chris Beer <chris@cbeer.info> - 5.2.1-1
- Initial package
