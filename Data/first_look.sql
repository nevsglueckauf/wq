SELECT sess_loc, sess_co_done,  count(*) as Anzahl, MIN(datum), MAX(datum)
FROM sessions
GROUP BY sess_loc
HAVING sess_co_done =1
ORDER by anzahl DESC;

SELECT sug_platform, datum, sessions, sess_co_done      FROM sessions

WHERE datum between '2025-02-01' AND '2025-02-28';


SELECT sug_platform, datum, sessions, sess_co_done      FROM sessions

WHERE datum between '2025-02-01' AND '2025-02-28'
AND sess_co_done =1 
ORDER By sessions DESC;