%define debug_package %{nil}
%define solr_install_dir %{_javadir}/solr
%define plugin_install_dir %{solr_install_dir}/plugins
%define plugin_name cjk-filter
%define solr_version 6.1.0

Name:           solr-%{plugin_name}
Version:        1.0.5
Release:        0%{?dist}
Summary:        A Lucene/Solr filter and filter factory to fold certain CJK characters to improve recall. 

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://github.com/sul-dlss/CJKFoldingFilter/
Source0:        https://github.com/sul-dlss/CJKFoldingFilter/releases/download/%{version}/CJKFoldingFilter.jar
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       solr >= %{solr_version}

Provides: %{name}

%description
A Lucene/Solr filter and filter factory to fold certain CJK characters to improve recall. 


%install
rm -rf $RPM_BUILD_ROOT

%{__mkdir} -p %{buildroot}%{plugin_install_dir}
%{__install} -p -m 755 %{SOURCE0} %{buildroot}%{plugin_install_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{plugin_install_dir}/*

%changelog
* Wed Jul 5 2017 Chris Beer <chris@cbeer.info> - 6.6.0-0
- Update to Solr 6.6.0

* Fri Aug 5 2016 Chris Beer <chris@cbeer.info> - 1.0.5
- Package v1.0.5
