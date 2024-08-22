Postmortem: Service Outage on User Authentication System
Issue Summary
Duration: August 19, 2024, 14:30 EAT to August 19, 2024, 16:45 EAT
Impact: The User Authentication Service was intermittently failing, causing users to experience login errors. Approximately 35% of users were unable to access their accounts during the outage.
Root Cause: A misconfigured load balancer was directing traffic to an overwhelmed backend server.
Timeline
14:30 EAT: The issue was detected when multiple users reported login failures through the customer support channel.
14:32 EAT: Monitoring alerts indicated increased error rates and server response times.
14:45 EAT: The team began investigating the issue, initially focusing on backend server logs and database performance, suspecting a possible database bottleneck.
15:00 EAT: Misleading investigation led the team to incorrectly assume a database lock issue was causing the failures.
15:15 EAT: Incident escalated to the Site Reliability Engineering (SRE) team after initial checks did not resolve the issue.
15:30 EAT: SRE team identified the misconfigured load balancer as the root cause. Traffic was being routed disproportionately to one server, causing it to become overwhelmed.
15:45 EAT: The load balancer configuration was corrected, redistributing traffic evenly among backend servers.
16:00 EAT: The User Authentication Service was restored to full functionality as user login issues resolved.
16:45 EAT: Monitoring confirmed system stability and normal user login rates.
Root Cause and Resolution
Root Cause: The root cause of the outage was a misconfigured load balancer that failed to distribute traffic evenly across the backend servers. This caused one server to handle an excessive load, resulting in timeouts and failed login attempts for users.
Resolution: The load balancer configuration was updated to ensure proper traffic distribution. This adjustment balanced the load across all available servers, which alleviated the strain on the previously overloaded server and restored normal operation.
Corrective and Preventative Measures
Improvements:
Review Load Balancer Configuration: Implement stricter validation and review procedures for load balancer configurations.
Enhanced Monitoring: Improve monitoring to include more granular metrics on load balancer performance and backend server load.
Tasks:
Update Load Balancer Configuration: Ensure that the load balancer is properly configured with even traffic distribution.
Add Load Balancer Alerts: Implement alerts for unusual traffic patterns and server load imbalances.
Conduct Load Testing: Regularly perform load testing to verify that the system can handle expected traffic volumes.
Document Configuration Changes: Maintain detailed documentation of all configuration changes for faster troubleshooting and recovery.
Review and Improve Incident Response: Evaluate incident response procedures to reduce the time to identify and resolve similar issues in the future.


