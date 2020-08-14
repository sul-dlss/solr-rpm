%define debug_package %{nil}
%define base_install_dir %{_javadir}/%{name}
%define solr_group solr
%define solr_user solr
%define __jar_repack 0

Name:           solr
Version:        8.6.1
Release:        0%{?dist}
Summary:        A distributed, highly available, RESTful search engine

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            http://lucene.apache.org/solr/
Source0:        http://archive.apache.org/dist/lucene/solr/%{version}/solr-%{version}.tgz
Source1:        systemd-solr
Source2:        sysconfig-solr
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  systemd

Requires:       jpackage-utils
Requires:       jre >= 1.7.0
Requires:       lsof

Requires(post): chkconfig initscripts
Requires(pre):  chkconfig initscripts
Requires(pre):  shadow-utils

Provides: solr

%description
A distributed, highly available, RESTful search engine

%prep
%setup -q -n %{name}-%{version}

%build
true

%install
rm -rf $RPM_BUILD_ROOT

#bin
%{__mkdir} -p %{buildroot}%{base_install_dir}/bin
%{__install} -p -m 755 bin/oom_solr.sh %{buildroot}%{base_install_dir}/bin
%{__install} -p -m 755 bin/post %{buildroot}%{base_install_dir}/bin
%{__install} -p -m 755 bin/solr %{buildroot}%{base_install_dir}/bin
%{__install} -p -m 644 bin/solr.in.sh %{buildroot}%{base_install_dir}/bin

# contrib
%{__mkdir} -p %{buildroot}%{base_install_dir}/contrib

# licenses
%{__mkdir} -p %{buildroot}%{base_install_dir}/licenses
%{__install} -p -m 644 licenses/* %{buildroot}%{base_install_dir}/licenses

#libs
%{__mkdir} -p %{buildroot}%{base_install_dir}/dist
%{__install} -p -m 644 dist/solr-analytics-*.jar %{buildroot}%{base_install_dir}/dist
%{__install} -p -m 644 dist/solr-cell-*.jar %{buildroot}%{base_install_dir}/dist
%{__install} -p -m 644 dist/solr-dataimporthandler-%{version}.jar %{buildroot}%{base_install_dir}/dist
%{__install} -p -m 644 dist/solr-core-*.jar %{buildroot}%{base_install_dir}/dist

# server libs
%{__mkdir} -p %{buildroot}%{base_install_dir}/server
%{__install} -p -m 644 server/*.jar %{buildroot}%{base_install_dir}/server

%{__mkdir} -p %{buildroot}%{base_install_dir}/server/contexts
%{__install} -p -m 644 server/contexts/*.xml %{buildroot}%{base_install_dir}/server/contexts

%{__mkdir} -p %{buildroot}%{base_install_dir}/server/etc
%{__install} -p -m 644 server/etc/*.xml %{buildroot}%{base_install_dir}/server/etc

%{__mkdir} -p %{buildroot}%{base_install_dir}/server/lib
%{__install} -p -m 644 server/lib/*.jar %{buildroot}%{base_install_dir}/server/lib

%{__mkdir} -p %{buildroot}%{base_install_dir}/server/lib/ext
%{__install} -p -m 644 server/lib/ext/*.jar %{buildroot}%{base_install_dir}/server/lib/ext

%{__mkdir} -p %{buildroot}%{base_install_dir}/server/modules
%{__install} -p -m 644 server/modules/*.mod %{buildroot}%{base_install_dir}/server/modules

%{__mkdir} -p %{buildroot}%{base_install_dir}/server/resources

%{__mkdir} -p %{buildroot}%{base_install_dir}/server/scripts/cloud-scripts
%{__install} -p -m 755 server/scripts/cloud-scripts/* %{buildroot}%{base_install_dir}/server/scripts/cloud-scripts

# webapp

%{__mkdir} -p %{buildroot}%{base_install_dir}/server/solr-webapp/webapp
%{__cp} -R -p server/solr-webapp/webapp/* %{buildroot}%{base_install_dir}/server/solr-webapp/webapp

# config
%{__mkdir} -p %{buildroot}%{_sysconfdir}/solr
%{__install} -p -m 644 server/solr/README.txt %{buildroot}%{_sysconfdir}/%{name}
%{__install} -p -m 644 server/solr/solr.xml %{buildroot}%{_sysconfdir}/%{name}
%{__install} -p -m 644 server/solr/zoo.cfg %{buildroot}%{_sysconfdir}/%{name}
%{__install} -p -m 644 server/resources/log4j2.xml %{buildroot}%{_sysconfdir}/%{name}
%{__install} -p -m 644 server/resources/log4j2-console.xml %{buildroot}%{_sysconfdir}/%{name}
ln -sf %{_sysconfdir}/%{name}/log4j2.xml %{buildroot}%{base_install_dir}/server/resources/log4j2.xml
ln -sf %{_sysconfdir}/%{name}/log4j2-console.xml %{buildroot}%{base_install_dir}/server/resources/log4j2-console.xml

%{__install} -p -m 644 server/resources/jetty-logging.properties %{buildroot}%{_sysconfdir}/%{name}
ln -sf %{_sysconfdir}/%{name}/jetty-logging.properties %{buildroot}%{base_install_dir}/server/resources/jetty-logging.properties

# data
%{__mkdir} -p %{buildroot}%{_localstatedir}/lib/%{name}
%{__mkdir} -p %{buildroot}%{_localstatedir}/lib/%{name}/lib
ln -sf %{_sysconfdir}/%{name}/solr.xml %{buildroot}%{_localstatedir}/lib/%{name}/solr.xml

# logs
%{__mkdir} -p %{buildroot}%{_localstatedir}/log/%{name}
ln -sf %{_localstatedir}/log/%{name} %{buildroot}%{base_install_dir}/server/logs

# plugins
%{__mkdir} -p %{buildroot}%{base_install_dir}/plugins

# sysconfig and init
%{__mkdir} -p %{buildroot}%{_unitdir}
%{__mkdir} -p %{buildroot}%{_sysconfdir}/sysconfig
%{__install} -m 755 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
%{__install} -m 755 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

%{__mkdir} -p %{buildroot}%{_localstatedir}/run/%{name}
%{__mkdir} -p %{buildroot}%{_localstatedir}/lock/subsys/%{name}

%pre
getent group %{solr_group} >/dev/null || groupadd -r %{solr_group}
getent passwd %{solr_user} >/dev/null || /usr/sbin/useradd --comment "Solr Daemon User" --shell /sbin/nologin -M -r -g %{solr_group} --home %{base_install_dir} %{solr_user}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%dir %{base_install_dir}
%{base_install_dir}/bin/*
%{base_install_dir}/dist/*
%{base_install_dir}/licenses/*
%docdir %{base_install_dir}/licenses
%{base_install_dir}/server/*
%dir %{base_install_dir}/plugins
%config(noreplace) %{_sysconfdir}/%{name}
%doc README.txt LICENSE.txt  NOTICE.txt  CHANGES.txt
%defattr(-,%{solr_user},%{solr_group},-)
%dir %{_localstatedir}/lib/%{name}
%{_localstatedir}/lib/%{name}/solr.xml
%dir %{_localstatedir}/lib/%{name}/lib
%{_localstatedir}/run/%{name}
%dir %{_localstatedir}/log/%{name}


%changelog
* Fri Aug 14 2020 Chris Beer <chris@cbeer.info> - 8.6.1-0
- Update to Solr 8.6.1

* Wed Jul 15 2020 Chris Beer <chris@cbeer.info> - 8.6.0-0
- Update to Solr 8.6.0

* Thu Jul 9 2020 Chris Beer <chris@cbeer.info> - 8.5.2-0
- Update to Solr 8.5.2

* Sat Aug 10 2019 Chris Beer <chris@cbeer.info> - 8.2.0-0
- Update to Solr 8.2.0

* Thu Aug 08 2019 Chris Beer <chris@cbeer.info> - 7.7.2-0
- Update to Solr 7.7.2

* Sat Feb 16 2019 Chris Beer <chris@cbeer.info> - 7.7.0-0
- Update to Solr 7.7.0

* Mon Dec 17 2018 Chris Beer <chris@cbeer.info> - 7.6.0-0
- Update to Solr 7.6.0

* Mon Sep 24 2018 Chris Beer <chris@cbeer.info> - 7.5.0-0
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

* Sat Aug 27 2016 Chris Beer <chris@cbeer.info> - 6.5.1-0
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
