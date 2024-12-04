%%  MATLAB PYTHON DATA COMMUNICATION
%%
% Create a TCP/IP server
server = tcpserver('127.0.0.1', 65432);  % Localhost on port 65432
disp('Server is ready. Waiting for connection...');

while true
    % Wait for data from Python
    if server.NumBytesAvailable > 0
        data = readline(server);  % Read incoming data as a string
        disp(['Received from Python: ', data]);

        % Send a response back to Python
        response = "Hello from MATLAB!";
        writeline(server, response);
        disp(['Sent to Python: ', response]);
        break; % Exit after one exchange
    end
end

% Configure serial port
serialPort = 'COM3'; % Replace 'COM3' with your serial port
baudRate = 9600;

s = serial(serialPort, 'BaudRate', baudRate, 'Terminator', 'LF');
fopen(s);

disp('Waiting for data...');

while true
    if s.BytesAvailable > 0
        % Read data from Python
        data = fscanf(s);  % Read data from serial port
        disp(['Received: ', data]);

        % Send response back to Python
        response = "Hello from MATLAB!";
        fprintf(s, response);
        disp(['Sent: ', response]);
        break; % Exit after one exchange
    end
end

fclose(s);
delete(s);
clear s;


%%
%% MATLAB PYTHON SERIAL COMMUNICATION
% USE VIRTUAL SERIAL PORT FOR COMMUNICATION
% Configure serial port
serialPort = 'COM2'; % Replace with your serial port
baudRate = 115200;

s = serial(serialPort, 'BaudRate', baudRate, 'Terminator', 'LF');
fopen(s);

disp('Waiting for command...');

while true
    if s.BytesAvailable > 0
        % Read command from Python
        command = fscanf(s, '%s');  % Read string from the serial port
        disp(['Received command: ', command]);
        
        % Execute the received command
        try
            eval(command);  % Execute the MATLAB command
            disp(['Executed command: ', command]);
            
            % Send acknowledgment back to Python
            response = "Command executed successfully!";
            fprintf(s, response);
        catch ME
            % Send error message back to Python if command fails
            response = ['Error executing command: ', ME.message];
            fprintf(s, response);
        end
        break; % Exit after processing one command
    end
end

fclose(s);
delete(s);
clear s;
