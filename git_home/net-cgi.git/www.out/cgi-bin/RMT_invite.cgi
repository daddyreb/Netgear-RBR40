#!/bin/sh
. /www/cgi-bin/func.sh
eval "`/www/cgi-bin/proccgi $*`"
refreshed_page="/cgi-bin/RMT_invite.htm"

#SYS_PREFIX=$(${nvram} get leafp2p_sys_prefix)

EXEC_RESULT="register_fail"

#cd "${SYS_PREFIX}/bin"
#. "/opt/rcagent/scripts/comm.sh"
if [ -f /www/cgi-bin/readycloud_control.cgi ];then
case "$FORM_submit_flag" in
	register_user)
		echo "{\"state\":\"1\",\"owner\":\"$FORM_TXT_remote_login\",\"password\":\"$FORM_TXT_remote_passwd\"}"|REQUEST_METHOD=PUT PATH_INFO=/api/services/readycloud /www/cgi-bin/readycloud_control.cgi  > /dev/console
		RESULT=$(${nvram} get readycloud_registration_owner)

		if [ "x$RESULT" = "x" ]; then
			sleep 3
			echo "{\"state\":\"1\",\"owner\":\"$FORM_TXT_remote_login\",\"password\":\"$FORM_TXT_remote_passwd\"}"|REQUEST_METHOD=PUT PATH_INFO=/api/services/readycloud /www/cgi-bin/readycloud_control.cgi  > /dev/console
			RESULT=$(${nvram} get readycloud_registration_owner)
		fi

		if [ "x$RESULT" = "x" ]; then
			EXEC_RESULT="register_fail"
		else
			OLD_USER_NAME=$(${nvram} get readycloud_user_admin)
			${nvram} set readycloud_enable=1
			if [ "x$FORM_TXT_remote_login" != "x$OLD_USER_NAME" ]; then
				${nvram} set readycloud_user_admin=$FORM_TXT_remote_login
			fi

			EXEC_RESULT="register_ok"

			if [ "$FORM_change_wan_pppoe_demand" = "1" ]; then
				${nvram} set wan_pppoe_demand=0;
			fi
			if [ "$FORM_change_wan_pptp_demand" = "1" ]; then
				${nvram} set wan_pptp_demand=0;
			fi
			if [ "$FORM_change_wan_mulpppoe_demand" = "1" ]; then
				${nvram} set wan_mulpppoe_demand=0;
			fi
			if [ "$FORM_change_wan_l2tp_demand" = "1" ]; then
				${nvram} set wan_l2tp_demand=0;
			fi
		fi
	;;
    unregister_user)
    		echo "{\"state\":\"0\",\"owner\":\"$FORM_TXT_remote_login\",\"password\":\"x\"}"|REQUEST_METHOD=PUT PATH_INFO=/api/services/readycloud /www/cgi-bin/readycloud_control.cgi > /dev/console
		RESULT=$(${nvram} get readycloud_registration_owner)
		if [ "x$RESULT" = "x" ]; then
			${nvram} set readycloud_enable=0
			EXEC_RESULT="unreg_ok"
		else
			EXEC_RESULT="unreg_fail"
		fi
	;;
esac
fi
#HTTP_URL=`echo ${HTTP_HOST} | sed '$s/.$//' `
#uncomment the last line above, because we save HTTP_HOST in our router is just numbers . no \r\n or \n kind of thing. otherwise the HTTP_HOST will be removed the last number.(ep 192.168.1.1 --> 192.168.1.) and return error.
HTTP_URL=`echo ${HTTP_HOST} `
print_http_refresh "${refreshed_page}?${EXEC_RESULT}" "0"

exec >&-
