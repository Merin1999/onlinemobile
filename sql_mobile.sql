/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.4.24-MariaDB : Database - mobile_store
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`mobile_store` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `mobile_store`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `auth_group` */

LOCK TABLES `auth_group` WRITE;

UNLOCK TABLES;

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `auth_group_permissions` */

LOCK TABLES `auth_group_permissions` WRITE;

UNLOCK TABLES;

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4;

/*Data for the table `auth_permission` */

LOCK TABLES `auth_permission` WRITE;

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add booking',7,'add_booking'),(26,'Can change booking',7,'change_booking'),(27,'Can delete booking',7,'delete_booking'),(28,'Can view booking',7,'view_booking'),(29,'Can add category',8,'add_category'),(30,'Can change category',8,'change_category'),(31,'Can delete category',8,'delete_category'),(32,'Can view category',8,'view_category'),(33,'Can add dealer',9,'add_dealer'),(34,'Can change dealer',9,'change_dealer'),(35,'Can delete dealer',9,'delete_dealer'),(36,'Can view dealer',9,'view_dealer'),(37,'Can add login',10,'add_login'),(38,'Can change login',10,'change_login'),(39,'Can delete login',10,'delete_login'),(40,'Can view login',10,'view_login'),(41,'Can add product',11,'add_product'),(42,'Can change product',11,'change_product'),(43,'Can delete product',11,'delete_product'),(44,'Can view product',11,'view_product'),(45,'Can add ramss',12,'add_ramss'),(46,'Can change ramss',12,'change_ramss'),(47,'Can delete ramss',12,'delete_ramss'),(48,'Can view ramss',12,'view_ramss'),(49,'Can add romss',13,'add_romss'),(50,'Can change romss',13,'change_romss'),(51,'Can delete romss',13,'delete_romss'),(52,'Can view romss',13,'view_romss'),(53,'Can add user',14,'add_user'),(54,'Can change user',14,'change_user'),(55,'Can delete user',14,'delete_user'),(56,'Can view user',14,'view_user'),(57,'Can add sub_category',15,'add_sub_category'),(58,'Can change sub_category',15,'change_sub_category'),(59,'Can delete sub_category',15,'delete_sub_category'),(60,'Can view sub_category',15,'view_sub_category'),(61,'Can add review',16,'add_review'),(62,'Can change review',16,'change_review'),(63,'Can delete review',16,'delete_review'),(64,'Can view review',16,'view_review'),(65,'Can add requests',17,'add_requests'),(66,'Can change requests',17,'change_requests'),(67,'Can delete requests',17,'delete_requests'),(68,'Can view requests',17,'view_requests'),(69,'Can add payment',18,'add_payment'),(70,'Can change payment',18,'change_payment'),(71,'Can delete payment',18,'delete_payment'),(72,'Can view payment',18,'view_payment'),(73,'Can add bookingchild',19,'add_bookingchild'),(74,'Can change bookingchild',19,'change_bookingchild'),(75,'Can delete bookingchild',19,'delete_bookingchild'),(76,'Can view bookingchild',19,'view_bookingchild'),(77,'Can add history',20,'add_history'),(78,'Can change history',20,'change_history'),(79,'Can delete history',20,'delete_history'),(80,'Can view history',20,'view_history');

UNLOCK TABLES;

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `auth_user` */

LOCK TABLES `auth_user` WRITE;

UNLOCK TABLES;

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `auth_user_groups` */

LOCK TABLES `auth_user_groups` WRITE;

UNLOCK TABLES;

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `auth_user_user_permissions` */

LOCK TABLES `auth_user_user_permissions` WRITE;

UNLOCK TABLES;

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `django_admin_log` */

LOCK TABLES `django_admin_log` WRITE;

UNLOCK TABLES;

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;

/*Data for the table `django_content_type` */

LOCK TABLES `django_content_type` WRITE;

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'main','booking'),(19,'main','bookingchild'),(8,'main','category'),(9,'main','dealer'),(20,'main','history'),(10,'main','login'),(18,'main','payment'),(11,'main','product'),(12,'main','ramss'),(17,'main','requests'),(16,'main','review'),(13,'main','romss'),(15,'main','sub_category'),(14,'main','user'),(6,'sessions','session');

UNLOCK TABLES;

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;

/*Data for the table `django_migrations` */

LOCK TABLES `django_migrations` WRITE;

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2023-02-21 07:38:32.939146'),(2,'auth','0001_initial','2023-02-21 07:38:33.567292'),(3,'admin','0001_initial','2023-02-21 07:38:33.763190'),(4,'admin','0002_logentry_remove_auto_add','2023-02-21 07:38:33.775905'),(5,'admin','0003_logentry_add_action_flag_choices','2023-02-21 07:38:33.781247'),(6,'contenttypes','0002_remove_content_type_name','2023-02-21 07:38:33.855623'),(7,'auth','0002_alter_permission_name_max_length','2023-02-21 07:38:33.924313'),(8,'auth','0003_alter_user_email_max_length','2023-02-21 07:38:33.944020'),(9,'auth','0004_alter_user_username_opts','2023-02-21 07:38:33.960182'),(10,'auth','0005_alter_user_last_login_null','2023-02-21 07:38:34.050966'),(11,'auth','0006_require_contenttypes_0002','2023-02-21 07:38:34.050966'),(12,'auth','0007_alter_validators_add_error_messages','2023-02-21 07:38:34.063672'),(13,'auth','0008_alter_user_username_max_length','2023-02-21 07:38:34.100156'),(14,'auth','0009_alter_user_last_name_max_length','2023-02-21 07:38:34.118319'),(15,'auth','0010_alter_group_name_max_length','2023-02-21 07:38:34.136728'),(16,'auth','0011_update_proxy_permissions','2023-02-21 07:38:34.153631'),(17,'auth','0012_alter_user_first_name_max_length','2023-02-21 07:38:34.170267'),(18,'main','0001_initial','2023-02-21 07:38:35.396257'),(19,'sessions','0001_initial','2023-02-21 07:38:35.449948'),(20,'main','0002_history','2023-03-03 10:27:40.954372');

UNLOCK TABLES;

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `django_session` */

LOCK TABLES `django_session` WRITE;

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('t2b81hr3bdi6nhfe13u5f4o95q5u2o6w','eyJsb2dpbl9pZCI6MSwibGxpZCI6NCwib3RwIjo0NjEwLCJkZWFsZXJfaWQiOjJ9:1pV3WD:Q8w5Qr7vRFT9Z3zMGOAVxgHDJoZPik3qYEoVIJn1esg','2023-03-09 04:47:45.589027'),('t6qymxniuuxjn2v1lcblh4ic6b2mo28t','eyJsb2dpbl9pZCI6NH0:1pY8MD:1K1GS9Lv9h1DwXGOXCJpjQecFOGIbRZR45Z3Y0TOdhc','2023-03-17 16:34:09.231592'),('t93gmsshkwmkud050ltbght74azw3j5n','eyJsb2dpbl9pZCI6NywiZGVhbGVyX2lkIjo0fQ:1pY4Do:Qg65oXDVSzJCpiZav09KxYDi3lVRuG0dHSdFP0h_Ntg','2023-03-17 12:09:12.266279'),('ujffbi5uo7jjkod396m8wpst54d5wq1m','eyJsb2dpbl9pZCI6MX0:1pY4eZ:POfqh5xyix0BZ2U6aLPUjjWAD8gnIphHKUe4LPafvOU','2023-03-17 12:36:51.446582');

UNLOCK TABLES;

/*Table structure for table `main_booking` */

DROP TABLE IF EXISTS `main_booking`;

CREATE TABLE `main_booking` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `total` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `order_id` varchar(50) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_booking_user_id_7fb45758_fk_main_user_id` (`user_id`),
  CONSTRAINT `main_booking_user_id_7fb45758_fk_main_user_id` FOREIGN KEY (`user_id`) REFERENCES `main_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_booking` */

LOCK TABLES `main_booking` WRITE;

insert  into `main_booking`(`id`,`total`,`date`,`status`,`order_id`,`user_id`) values (16,'150000','2023-03-03','pending','0',2);

UNLOCK TABLES;

/*Table structure for table `main_bookingchild` */

DROP TABLE IF EXISTS `main_bookingchild`;

CREATE TABLE `main_bookingchild` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `quantity` varchar(50) NOT NULL,
  `amount` varchar(50) NOT NULL,
  `booking_id` bigint(20) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_bookingchild_booking_id_7e2013bc_fk_main_booking_id` (`booking_id`),
  KEY `main_bookingchild_product_id_a4a761b5_fk_main_product_id` (`product_id`),
  CONSTRAINT `main_bookingchild_booking_id_7e2013bc_fk_main_booking_id` FOREIGN KEY (`booking_id`) REFERENCES `main_booking` (`id`),
  CONSTRAINT `main_bookingchild_product_id_a4a761b5_fk_main_product_id` FOREIGN KEY (`product_id`) REFERENCES `main_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_bookingchild` */

LOCK TABLES `main_bookingchild` WRITE;

insert  into `main_bookingchild`(`id`,`quantity`,`amount`,`booking_id`,`product_id`) values (17,'1','130000',16,8),(18,'1','20000',16,5);

UNLOCK TABLES;

/*Table structure for table `main_category` */

DROP TABLE IF EXISTS `main_category`;

CREATE TABLE `main_category` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `category` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_category` */

LOCK TABLES `main_category` WRITE;

insert  into `main_category`(`id`,`category`) values (1,'Mobiles'),(6,'Accessories');

UNLOCK TABLES;

/*Table structure for table `main_dealer` */

DROP TABLE IF EXISTS `main_dealer`;

CREATE TABLE `main_dealer` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `login_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_dealer_login_id_bae7d972_fk_main_login_id` (`login_id`),
  CONSTRAINT `main_dealer_login_id_bae7d972_fk_main_login_id` FOREIGN KEY (`login_id`) REFERENCES `main_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_dealer` */

LOCK TABLES `main_dealer` WRITE;

insert  into `main_dealer`(`id`,`company_name`,`place`,`phone`,`email`,`login_id`) values (2,'Apple','United Kingdom','6235634828','joseph457@gmail.com',5),(3,'Samsung','Delhi','9851235886','vishnu@gmail.com',6),(4,'Vivo','Mumbai','9856326991','vivo123@gmail.com',7),(5,'Oppo','Mumbai','9856321425','oppo@gmail.com',11);

UNLOCK TABLES;

/*Table structure for table `main_history` */

DROP TABLE IF EXISTS `main_history`;

CREATE TABLE `main_history` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_history_product_id_0cbd368a_fk_main_product_id` (`product_id`),
  KEY `main_history_user_id_ac04f9cc_fk_main_user_id` (`user_id`),
  CONSTRAINT `main_history_product_id_0cbd368a_fk_main_product_id` FOREIGN KEY (`product_id`) REFERENCES `main_product` (`id`),
  CONSTRAINT `main_history_user_id_ac04f9cc_fk_main_user_id` FOREIGN KEY (`user_id`) REFERENCES `main_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_history` */

LOCK TABLES `main_history` WRITE;

insert  into `main_history`(`id`,`date`,`product_id`,`user_id`) values (1,'2023-03-03',5,2);

UNLOCK TABLES;

/*Table structure for table `main_login` */

DROP TABLE IF EXISTS `main_login`;

CREATE TABLE `main_login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(1000) NOT NULL,
  `usertype` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_login` */

LOCK TABLES `main_login` WRITE;

insert  into `main_login`(`id`,`username`,`password`,`usertype`) values (1,'merin.21pmc141@mariancollege.org','admin','admin'),(2,'jinujose@gmail.com','Jinu@123','dealer'),(3,'merinjoseph457@gmail.comssss','Merin@123','pending'),(4,'merinjoseph457@gmail.com','Meri@123','user'),(5,'joseph457@gmail.com','nasi','dealer'),(6,'vishnu@gmail.com','Vishnu@123','dealer'),(7,'vivo123@gmail.com','Vivo@123','dealer'),(9,'alanbabu8886@gmail.com','Alan@123','pending'),(10,'nassihanazeer@gmail.com','Nasi@123','user'),(11,'oppo@gmail.com','Oppo@123','dealer');

UNLOCK TABLES;

/*Table structure for table `main_payment` */

DROP TABLE IF EXISTS `main_payment`;

CREATE TABLE `main_payment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `amount` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `booking_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_payment_booking_id_c230bf24_fk_main_booking_id` (`booking_id`),
  CONSTRAINT `main_payment_booking_id_c230bf24_fk_main_booking_id` FOREIGN KEY (`booking_id`) REFERENCES `main_booking` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_payment` */

LOCK TABLES `main_payment` WRITE;

UNLOCK TABLES;

/*Table structure for table `main_product` */

DROP TABLE IF EXISTS `main_product`;

CREATE TABLE `main_product` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(50) NOT NULL,
  `rate` varchar(50) NOT NULL,
  `stock` bigint(50) NOT NULL,
  `image` varchar(1000) NOT NULL,
  `p_description` varchar(1000) NOT NULL,
  `dealer_id` bigint(20) NOT NULL,
  `ram_id` bigint(20) NOT NULL,
  `rom_id` bigint(20) NOT NULL,
  `sub_category_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_product_ram_id_d2e0f93d_fk_main_ramss_id` (`ram_id`),
  KEY `main_product_rom_id_900b87b5_fk_main_romss_id` (`rom_id`),
  KEY `main_product_sub_category_id_a3344809_fk_main_sub_category_id` (`sub_category_id`),
  KEY `main_product_dealer_id_06e40d4a_fk_main_dealer_id` (`dealer_id`),
  CONSTRAINT `main_product_dealer_id_06e40d4a_fk_main_dealer_id` FOREIGN KEY (`dealer_id`) REFERENCES `main_dealer` (`id`),
  CONSTRAINT `main_product_ram_id_d2e0f93d_fk_main_ramss_id` FOREIGN KEY (`ram_id`) REFERENCES `main_ramss` (`id`),
  CONSTRAINT `main_product_rom_id_900b87b5_fk_main_romss_id` FOREIGN KEY (`rom_id`) REFERENCES `main_romss` (`id`),
  CONSTRAINT `main_product_sub_category_id_a3344809_fk_main_sub_category_id` FOREIGN KEY (`sub_category_id`) REFERENCES `main_sub_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_product` */

LOCK TABLES `main_product` WRITE;

insert  into `main_product`(`id`,`product_name`,`rate`,`stock`,`image`,`p_description`,`dealer_id`,`ram_id`,`rom_id`,`sub_category_id`) values (5,'Vivo Y 30','20000',4,'vivo y 30.jfif','Vivo Y30 smartphone was launched on 9th May 2020. The phone comes with a 6.47-inch touchscreen display with a resolution of 720×1560 pixels and an aspect ratio of 19.5:9. Vivo Y30 is powered by an octa-core MediaTek Helio P35 (MT6765) processor. It comes with 6GB of RAM. The Vivo Y30 runs Android 10 and is powered by a 5000mAh non-removable battery.',4,5,3,5),(6,'Back Cover','700',47,'case iphone.jfif','Amazon Brand - Solimo Slip-resistant Mobile Cover (Soft & Flexible Shockproof Back Case with Cushioned Edges) Transparent for Apple iPhone 11 Pro',2,3,2,6),(7,'Iphone 13','61999',98,'iphone13.webp',' Brand	Apple Model Name	IPhone Network Service Provider	Unlocked for All Carriers Operating System	IOS 14 Cellular Technology	5G About this item 15 cm (6.1-inch) Super Retina XDR display Cinematic mode adds shallow depth of field and shifts focus automatically in your videos Advanced dual-camera system with 12MP Wide and Ultra Wide cameras; Photographic Styles, Smart HDR 4, Night mode, 4K Dolby Vision HDR recording 12MP TrueDepth front camera with Night mode, 4K Dolby Vision HDR recording A15 Bionic chip for lightning-fast performance',2,5,3,6),(8,'Iphone 14 Pro max','130000',120,'14 pro max.jfif','A magical new way to interact with iPhone. A vital safety feature designed to save lives. An innovative 48MP camera for mind-blowing detail. All powered by the ultimate smartphone chip.',2,5,4,6);

UNLOCK TABLES;

/*Table structure for table `main_ram` */

DROP TABLE IF EXISTS `main_ram`;

CREATE TABLE `main_ram` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `ram` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_ram` */

LOCK TABLES `main_ram` WRITE;

insert  into `main_ram`(`id`,`ram`) values (2,'8GB'),(3,'6GB');

UNLOCK TABLES;

/*Table structure for table `main_ramss` */

DROP TABLE IF EXISTS `main_ramss`;

CREATE TABLE `main_ramss` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `rams` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_ramss` */

LOCK TABLES `main_ramss` WRITE;

insert  into `main_ramss`(`id`,`rams`) values (1,',j'),(2,',jh'),(3,'4'),(4,'6 gb'),(5,'8 Gb'),(6,'16GB'),(7,'2 gb');

UNLOCK TABLES;

/*Table structure for table `main_requests` */

DROP TABLE IF EXISTS `main_requests`;

CREATE TABLE `main_requests` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `qty` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `amount` varchar(50) NOT NULL,
  `rstatus` varchar(50) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_requests_product_id_7419f547_fk_main_product_id` (`product_id`),
  CONSTRAINT `main_requests_product_id_7419f547_fk_main_product_id` FOREIGN KEY (`product_id`) REFERENCES `main_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_requests` */

LOCK TABLES `main_requests` WRITE;

insert  into `main_requests`(`id`,`qty`,`date`,`amount`,`rstatus`,`product_id`) values (2,'10','2023-03-03','200000','Stock Added',5);

UNLOCK TABLES;

/*Table structure for table `main_review` */

DROP TABLE IF EXISTS `main_review`;

CREATE TABLE `main_review` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `rate` varchar(50) NOT NULL,
  `reviews` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_review_product_id_83bd84e4_fk_main_product_id` (`product_id`),
  KEY `main_review_user_id_ee71ed52_fk_main_user_id` (`user_id`),
  CONSTRAINT `main_review_product_id_83bd84e4_fk_main_product_id` FOREIGN KEY (`product_id`) REFERENCES `main_product` (`id`),
  CONSTRAINT `main_review_user_id_ee71ed52_fk_main_user_id` FOREIGN KEY (`user_id`) REFERENCES `main_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_review` */

LOCK TABLES `main_review` WRITE;

insert  into `main_review`(`id`,`rate`,`reviews`,`date`,`product_id`,`user_id`) values (3,'4','Nice product','2023-02-23',7,5);

UNLOCK TABLES;

/*Table structure for table `main_rom` */

DROP TABLE IF EXISTS `main_rom`;

CREATE TABLE `main_rom` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `rom` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_rom` */

LOCK TABLES `main_rom` WRITE;

insert  into `main_rom`(`id`,`rom`) values (2,'8GB');

UNLOCK TABLES;

/*Table structure for table `main_romss` */

DROP TABLE IF EXISTS `main_romss`;

CREATE TABLE `main_romss` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `roms` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_romss` */

LOCK TABLES `main_romss` WRITE;

insert  into `main_romss`(`id`,`roms`) values (1,'hjg'),(2,'64'),(3,'128 Gb'),(4,'236 gb');

UNLOCK TABLES;

/*Table structure for table `main_sub_category` */

DROP TABLE IF EXISTS `main_sub_category`;

CREATE TABLE `main_sub_category` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `subcategory` varchar(50) NOT NULL,
  `category_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_sub_category_category_id_10c6d991_fk_main_category_id` (`category_id`),
  CONSTRAINT `main_sub_category_category_id_10c6d991_fk_main_category_id` FOREIGN KEY (`category_id`) REFERENCES `main_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_sub_category` */

LOCK TABLES `main_sub_category` WRITE;

insert  into `main_sub_category`(`id`,`subcategory`,`category_id`) values (2,'Realme',1),(3,'Poco M2 Pro',1),(4,'Realme 10',1),(5,'Vivo',1),(6,'Iphone',1),(7,'Redmi',1),(9,'Oppo',1);

UNLOCK TABLES;

/*Table structure for table `main_user` */

DROP TABLE IF EXISTS `main_user`;

CREATE TABLE `main_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `pincode` varchar(50) NOT NULL,
  `login_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_user_login_id_82508863_fk_main_login_id` (`login_id`),
  CONSTRAINT `main_user_login_id_82508863_fk_main_login_id` FOREIGN KEY (`login_id`) REFERENCES `main_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_user` */

LOCK TABLES `main_user` WRITE;

insert  into `main_user`(`id`,`fname`,`lname`,`place`,`phone`,`email`,`pincode`,`login_id`) values (1,'MERIN','JOSEPH','Mundakkayam','6235634828','merinjoseph457@gmail.comsss','685532',3),(2,'MERIN','JOSEPH','Mundakkayam','9746532668','merinjoseph457@gmail.com','685532',4),(4,'Alan','Babu','Delhi','9323563482','alanbabu8886@gmail.com','685532',9),(5,'Nassiha','Nazeer','Delhi','9856217845','nassihanazeer@gmail.com','652359',10);

UNLOCK TABLES;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
