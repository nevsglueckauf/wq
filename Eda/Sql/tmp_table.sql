-- cr definition

CREATE TABLE cr (
	datum NVARCHAR(50),
	sessions INTEGER,
	sess_cart INTEGER,
	sess_co INTEGER,
	sess_co_done INTEGER,
	c_r REAL,
	dat_old NVARCHAR(50),
	sess_old INTEGER,
	sess_cart_add_old INTEGER,
	sess_co_old INTEGER,
	sess_co_done_old INTEGER
);

-- "products.csv" definition

CREATE TABLE "products.csv" (
	prod_name VARCHAR(128),
	prod_var VARCHAR(50),
	prod_var_sku VARCHAR(50),
	invent_start INTEGER,
	invent_end INTEGER,
	sold_units INTEGER,
	sell_rate INTEGER,
	invent_start_prev INTEGER,
	invent_end_prev INTEGER,
	sold_units_prev INTEGER,
	sell_rate_prev VARCHAR(50)
);

-- sales_per_channel definition

CREATE TABLE sales_per_channel (
	Tag VARCHAR(50),
	Vertriebskanal VARCHAR(50),
	Bestellungen INTEGER,
	Bruttoumsatz INTEGER,
	Rabatte INTEGER,
	Rückgaben INTEGER,
	Nettoumsatz INTEGER,
	Versandgebühren REAL,
	Steuern INTEGER,
	Gesamtumsatz REAL
);

-- sessions definition

CREATE TABLE sessions (
	sess_ctry VARCHAR(50),
	sess_loc VARCHAR(50),
	datum NVARCHAR(50),
	sug_platform VARCHAR(50),
	landing_uri VARCHAR(256),
	session_duration REAL,
	pages_per_sess REAL,
	jump_offs INTEGER,
	sess_cart_add INTEGER,
	sess_co INTEGER,
	sess_co_done INTEGER,
	sessions INTEGER
);

-- umsatz definition

CREATE TABLE umsatz (
	datum NVARCHAR(50),
	orders INTEGER,
	gross_turns REAL,
	discounts REAL,
	"returns" INTEGER,
	net_turns REAL,
	shippings REAL,
	duties INTEGER,
	add_rates INTEGER,
	taxes INTEGER,
	total_turn REAL,
	clients INTEGER,
	datum_prev NVARCHAR(50),
	orders_prev INTEGER,
	gross_sales_prev INTEGER,
	discounts_prev INTEGER,
	returns_prev INTEGER,
	net_turns_prev INTEGER,
	shippings_prev INTEGER,
	duties_prev INTEGER,
	add_rates_prev INTEGER,
	taxes_prev INTEGER,
	total_turn_prev INTEGER,
	clients_prev INTEGER
);