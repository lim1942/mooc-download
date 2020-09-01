var Destm = function(e, t) {
	function r(e, t) {
		var r = "";
		if ("object" == typeof e) for (var n in e) r += String.fromCharCode(e[n]);
		e = r || e;
		for (var i, o, a = new Uint8Array(e.length), s = t.length, n = 0; n < e.length; n++) o = n % s,
		    i = e[n],
			    i = i.toString().charCodeAt(0),
			      a[n] = i ^ t.charCodeAt(o);
		return a;
	}
	function n(e) {
		var t = "";
		if ("object" == typeof e) for (var r in e) t += String.fromCharCode(e[r]);
		e = t || e;
		var n = new Uint8Array(e.length);
		for (r = 0; r < e.length; r++) n[r] = e[r].toString().charCodeAt(0);
		var i, o, r = 0;
		for (r = 0; r < n.length; r++) i = n[r] % 3,
		    0 != i && r + i < n.length && (o = n[r + 1], n[r + 1] = n[r + i], n[r + i] = o, r = r + i + 1);
		return n;
	}
	function i(e) {
		var t = "";
		if ("object" == typeof e) for (var r in e) t += String.fromCharCode(e[r]);
		e = t || e;
		var n = new Uint8Array(e.length);
		for (r = 0; r < e.length; r++) n[r] = e[r].toString().charCodeAt(0);
		var r = 0,
			i = 0,
			  o = 0,
			  a = 0;
		for (r = 0; r < n.length; r++) o = n[r] % 2,
		    o && r++,
			    a++;
		var s = new Uint8Array(a);
		for (r = 0; r < n.length; r++) o = n[r] % 2,
		    o ? s[i++] = n[r++] : s[i++] = n[r];
		return s;
	}
	function o(e, t) {
		var r = 0,
		    n = 0,
		    i = 0,
		    o = 0,
		    a = "";
		if ("object" == typeof e) for (var r in e) a += String.fromCharCode(e[r]);
		e = a || e;
		var s = new Uint8Array(e.length);
		for (r = 0; r < e.length; r++) s[r] = e[r].toString().charCodeAt(0);
		for (r = 0; r < e.length; r++) if (o = s[r] % 5, 0 != o && 1 != o && r + o < s.length && (i = s[r + 1], n = r + 2, s[r + 1] = s[r + o], s[o + r] = i, r = r + o + 1, r - 2 > n)) for (; n < r - 2; n++) s[n] = s[n] ^ t.charCodeAt(n % t.length);
		for (r = 0; r < e.length; r++) s[r] = s[r] ^ t.charCodeAt(r % t.length);
		return s;
	}
	function a(e) {
		var t, r, n, i, o, a, s;
		for (a = e.length, o = 0, s = ""; o < a;) {
			do t = f[255 & e.charCodeAt(o++)];
			while (o < a && t == -1);
			if (t == -1) break;
			do r = f[255 & e.charCodeAt(o++)];
			while (o < a && r == -1);
			if (r == -1) break;
			s += String.fromCharCode(t << 2 | (48 & r) >> 4);
			do {
				if (n = 255 & e.charCodeAt(o++), 61 == n) return s;
				n = f[n]
			} while ( o < a && n == - 1 );
			if (n == -1) break;
			s += String.fromCharCode((15 & r) << 4 | (60 & n) >> 2);
			do {
				if (i = 255 & e.charCodeAt(o++), 61 == i) return s;
				i = f[i]
			} while ( o < a && i == - 1 );
			if (i == -1) break;
			s += String.fromCharCode((3 & n) << 6 | i)
		}
		return s
	}
	for (var s = {
		data: {
			info: e
		}
	},
	l = {
		q: r,
	    h: n,
	    m: i,
	    k: o
	},
	u = s.data.info, c = u.substring(u.length - 4).split(""), d = 0; d < c.length; d++) c[d] = c[d].toString().charCodeAt(0) % 4;
	c.reverse();
	for (var h = [], d = 0; d < c.length; d++) h.push(u.substring(c[d] + 1, c[d] + 2)),
	    u = u.substring(0, c[d] + 1) + u.substring(c[d] + 2);
	s.data.encrypt_table = h,
		s.data.key_table = [];
	for (var d in s.data.encrypt_table)"q" != s.data.encrypt_table[d] && "k" != s.data.encrypt_table[d] || (s.data.key_table.push(u.substring(u.length - 12)), u = u.substring(0, u.length - 12));
	s.data.key_table.reverse(),
		s.data.info = u;
	var f = new Array(( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), 62, ( - 1), ( - 1), ( - 1), 63, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), ( - 1), 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, ( - 1), ( - 1), ( - 1), ( - 1), ( - 1));
	s.data.info = a(s.data.info);
	for (var d in s.data.encrypt_table) {
		var p = s.data.encrypt_table[d];
		if ("q" == p || "k" == p) {
			var v = s.data.key_table.pop();
			s.data.info = l[s.data.encrypt_table[d]](s.data.info, v)
		} else s.data.info = l[s.data.encrypt_table[d]](s.data.info)
	}
	if (t) return s.data.info;
	var g = "";
	for (d = 0; d < s.data.info.length; d++) g += String.fromCharCode(s.data.info[d]);
	return g;
};