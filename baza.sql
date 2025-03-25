CREATE TABLE BooksCollection
(
    BookId INT IDENTITY(1000,1) NOT NULL PRIMARY KEY,
    BookTitle NVARCHAR(255) NOT NULL,
    AuthorName NVARCHAR(100) NOT NULL,
    Category NVARCHAR(50) NULL,
    PublisherName NVARCHAR(100) NULL,
    YearOfPublication SMALLINT NOT NULL CHECK (YearOfPublication BETWEEN 1000 AND YEAR(GETDATE())),
    ISBNCode VARCHAR(20) NOT NULL UNIQUE,
    AvailabilityStatus BIT NOT NULL DEFAULT 1,
    EditionNumber TINYINT NULL,
    TotalPages INT NULL,
    LanguageCode CHAR(2) NULL,
    BookDescription NVARCHAR(MAX) NULL,
    CoverImageLink VARCHAR(255) NULL,
    DateAdded DATETIME NOT NULL DEFAULT GETDATE(),
    LastUpdated DATETIME NULL,
    CONSTRAINT CHK_ISBN_Format CHECK (ISBNCode LIKE '[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]-[0-9]' OR 
                                      ISBNCode LIKE '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')
);
