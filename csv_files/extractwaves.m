 db = load('pwdb_data.mat');
 waves = db.data.waves;
 waves;
 
%  for i = 1:numel(fields)
%   teststruct.(fields{i})
% end

fields = fieldnames(waves);

for i=1:numel(fields)
 waveset = waves.(fields{i});
 fieldname = fields{i};
%   if strcmp(fields({i}), 'fs' )
%   fieldname = string(fields({i}));
  if strcmp(fieldname, 'P_Carotid')
      for j = 1:length(waveset)
        waveform = cell2mat(waveset(j));
        filename = sprintf('%s%d%s', 'myfile', j, '.csv');
        csvwrite(filename, transpose(waveform),0,0)
      end
  end
%   csvwrite('myFile.txt',waves.(fields{i}),0,0)
end