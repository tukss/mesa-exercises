function ret=mesa_profile(fn)
	fid = fopen(fn);

	fgets(fid);

	slabels = strsplit(fgets(fid));
	svalues = strsplit(fgets(fid));
	
	fgets(fid);
	fgets(fid);

	labels = strsplit(fgets(fid));
	fclose(fid);

	labels = labels(2:end-1);
	data = readtable('profile20.data','Headerlines',6,'FileType','text');
	data.Properties.VariableNames(1:end-1) = labels;
	ret = table2struct(data,'ToScalar',true);
	ret = rmfield(ret, labels(end));
        fields = fieldnames(ret)
        for i=1:length(fields)
                f = char(fields(i))
                ret.(f) = ret.(f)(end:-1:1)
	for i=2:length(slabels)-1
		ret.(char(slabels(i))) = sscanf(char(svalues(i)),'%f');
	end
end
