SELECT OUTS.ANIMAL_ID, OUTS.NAME from ANIMAL_OUTS OUTS
LEFT OUTER JOIN ANIMAL_INS INS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.ANIMAL_ID is NULL
ORDER BY OUTS.ANIMAL_ID ASC