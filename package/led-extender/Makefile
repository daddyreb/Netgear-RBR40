# 
# Copyright (C) 2008 Delta Networks Inc.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=led-extender
PKG_RELEASE:=1

PKG_BUILD_DIR := $(BUILD_DIR)/$(PKG_NAME)

include $(INCLUDE_DIR)/package.mk

define Package/led-extender
  SECTION:=utils
  CATEGORY:=Base system
  DEFAULT:=y
  TITLE:=Update utility for LED control
endef

define Build/Prepare
	mkdir -p $(PKG_BUILD_DIR)
	$(CP) ./src/* $(PKG_BUILD_DIR)/
endef

define Build/Compile
endef

define Package/led-extender/install
	install -d -m0755 $(1)/sbin
	install -m0755 $(PKG_BUILD_DIR)/led-extender $(1)/sbin/
	install -m0755 $(PKG_BUILD_DIR)/led-extender-5G $(1)/sbin/
	install -m0755 $(PKG_BUILD_DIR)/scan_result_process $(1)/sbin/
	install -m0755 ./files/renew-ip $(1)/sbin/
	install -m0755 ./files/renew-chan $(1)/sbin/
	install -m0755 ./files/set-tmp-chan $(1)/sbin/
	install -m0755 ./files/wlan_scan $(1)/sbin/
	install -m0755 ./files/get_channel $(1)/sbin/
	install -m0755 ./files/set-countryregion $(1)/sbin/
	install -m0755 ./files/rm_wps_link $(1)/sbin/
	install -m0755 ./files/repeater_wps $(1)/sbin/
	install -m0755 ./files/disable_dhcp $(1)/sbin/
endef

$(eval $(call BuildPackage,led-extender))
