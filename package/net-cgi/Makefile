# 
# Copyright (C) 2009 OpenWrt.org
#

include $(TOPDIR)/rules.mk

PKG_NAME:=net-cgi
PKG_RELEASE:=1
PKG_BUILD_DIR := $(BUILD_DIR)/$(PKG_NAME)

WEB_PATH:=www
WEB_PATH_CC:=www.satellite

include $(INCLUDE_DIR)/package.mk

PKG_GIT_TREEISH:=orbi-gui-dni011

define Package/net-cgi
  SECTION:=utils
  CATEGORY:=Base system
  DEFAULT:=y
  TITLE:=The mini_httpd CGI interface
endef

define Build/Prepare
	$(CP) $(GIT_HOME)/net-cgi.git/* $(PKG_BUILD_DIR)/
endef

define Build/Compile
endef

define Build/Configure
endef
define Package/net-cgi/install
	$(MAKE) -C $(PKG_BUILD_DIR) install INS_DIR_PRE=$(1)

	$(INSTALL_BIN) $(PKG_BUILD_DIR)/files/support_soap_list $(TOPDIR)/bin/

	$(LN) /tmp/openvpn/windows.zip $(1)/$(WEB_PATH)/windows.zip
	$(LN) /tmp/openvpn/nonwindows.zip $(1)/$(WEB_PATH)/nonwindows.zip
	$(LN) /tmp/openvpn/smart_phone.zip $(1)/$(WEB_PATH)/smart_phone.zip
	$(INSTALL_DIR) $(1)/sbin
	$(INSTALL_BIN) ./files/dni_wlan $(1)/sbin/
endef

$(eval $(call BuildPackage,net-cgi))
