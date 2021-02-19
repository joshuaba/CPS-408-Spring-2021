SELECT FirstName, LastName, Email FROM Employee;

SELECT * FROM Artist;

SELECT * FROM Employee WHERE Title LIKE '%M%r';

-- 4) SELECT * FROM Invoice WHERE max(Total)

SELECT BillingAddress, BillingCity, BillingPostalCode, Total FROM Invoice WHERE Billingcountry = 'Germany';

SELECT BillingAddress, BillingCity, BillingPostalCode, Total FROM Invoice WHERE Total < 25 AND Total > 15;

SELECT DISTINCT BillingCountry FROM Invoice;

SELECT FirstName, LastName, CustomerId, Country FROM Customer WHERE Country != 'USA';

SELECT * FROM Customer WHERE Country = 'Brazil';

select t.Name, il.* from InvoiceLine as il inner join Track as t on il.TrackId = t.TrackId order by t.Name;


