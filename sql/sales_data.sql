-- Create the database
CREATE DATABASE IF NOT EXISTS sales_data;
USE sales_data;

-- Create the Accounts table
CREATE TABLE IF NOT EXISTS Accounts (
    account VARCHAR(255) PRIMARY KEY,
    sector VARCHAR(255),
    year_established INT,
    revenue DECIMAL(10, 2),
    employees INT,
    office_location VARCHAR(255),
    subsidiary_of VARCHAR(255)
);

-- Create the Sales Teams table
CREATE TABLE IF NOT EXISTS Sales_Teams (
    sales_agent VARCHAR(255) PRIMARY KEY,
    manager VARCHAR(255),
    regional_office VARCHAR(255)
);

-- Create the Products table
CREATE TABLE IF NOT EXISTS Products (
    product VARCHAR(255) PRIMARY KEY,
    series VARCHAR(255),
    sales_price DECIMAL(10, 2)
);

-- Create the Sales Pipeline table
CREATE TABLE IF NOT EXISTS Sales_Pipeline (
    opportunity_id VARCHAR(255) PRIMARY KEY,
    sales_agent VARCHAR(255),
    product VARCHAR(255),
    account VARCHAR(255)  DEFAULT NULL,
    deal_stage VARCHAR(50),
    engage_date DATE DEFAULT NULL,
    close_date DATE DEFAULT NULL,
    close_value DECIMAL(10, 0) DEFAULT NULL,
    FOREIGN KEY (sales_agent) REFERENCES Sales_Teams(sales_agent),
    FOREIGN KEY (product) REFERENCES Products(product),
    FOREIGN KEY (account) REFERENCES Accounts(account)
);


