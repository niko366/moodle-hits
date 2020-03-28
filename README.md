# moodle-hits
python sederhana untuk mengetahui aktivitas pengunjung seperti active user,page view,unique ip multisite moodle

buat tabel "app1_moodleconfig"
CREATE TABLE IF NOT EXISTS `app1_moodleconfig` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nama_sekolah` varchar(50) NOT NULL,
  `hostname` varchar(100) NOT NULL,
  `db_name` varchar(50) NOT NULL,
  `username` varchar(32) NOT NULL,
  `password` varchar(32) NOT NULL,
  `ssh_port` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
kemudian isi credential database masing-masing moodle

buat tabel "a_hits" untuk menampung data hit
CREATE TABLE IF NOT EXISTS `a_hits` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sekolah` varchar(30) NOT NULL,
  `unique_user` int(11) NOT NULL,
  `unique_page_request` int(11) NOT NULL,
  `unique_ip` int(11) NOT NULL,
  `time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;

run : python data_lms.py
sekolah         unique userid	page requests	unique ip	time 	
smpn 4 jakarta  249 	23247 	159 	2016-04-01 11:01:48
sman 69 jakarta 197 	20068 	167 	2017-02-02 01:31:33
sman 1 bekasi   327 	24092 	113 	2017-08-03 05:06:49
smak 1 penabur  15 	  1687 	  86 	  2016-11-04 06:30:57
smp apasaja     15 	  731 	  78 	  2016-10-05 07:47:25
stm jakarta     22 	  1820 	  101 	2017-02-06 00:49:45
sman 6 jakarta  42 	  4798 	  122 	 2017-07-07 02:49:54

versi Django coming soon

