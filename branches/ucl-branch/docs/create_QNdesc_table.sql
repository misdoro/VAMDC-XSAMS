CREATE TABLE QNdesc (
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    caseID SMALLINT UNSIGNED,
    case_prefix VARCHAR(32),
    name VARCHAR(32),
    HTMLname VARCHAR(64),
    LaTeXname VARCHAR(64),
    attributes TEXT,
    HTMLattributes TEXT,
    LaTeXattributes TEXT,
    description TEXT,
    HTMLdescription TEXT,
    LaTeXdescription TEXT,
    restrictions TEXT,
    HTMLrestrictions TEXT,
    LaTeXrestrictions TEXT,
    KEY quantum_number (caseID,name)
)
