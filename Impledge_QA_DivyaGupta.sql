-- Update the admissions table
UPDATE [Admissions]
SET attending_doctor_id = 29
WHERE attending_doctor_id = 3;

UPDATE [Admissions]
SET patient_id = 4
WHERE patient_id = 35;

SELECT COUNT(*)
FROM Admissions
WHERE attending_doctor_id = 3;

-- Query 1: Doctors who have admissions
SELECT DISTINCT d.*
FROM doctors d
JOIN admissions a
ON d.doctor_id = a.attending_doctor_id;

-- Query 2: Doctors with no admissions
SELECT d.*
FROM doctors d
LEFT JOIN admissions a
ON d.doctor_id = a.attending_doctor_id
WHERE a.attending_doctor_id IS NULL;

-- Query 3: Patients whose admission can’t be completed due to missing doctor details
SELECT p.*
FROM patients p
JOIN admissions a
ON p.patient_id = a.patient_id
WHERE a.attending_doctor_id IS NULL;
